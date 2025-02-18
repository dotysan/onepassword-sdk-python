#!/bin/bash

# Helper script to release the Python SDK

set -e

# The list of python verisons the SDKs release for
python_versions=("$@")

# Minimum glibc version we support
glibc_version=2-32

# These versions are being supported due to the SDKs supporting Python 3.9+
macOS_version_x86_64=10.9
macOS_version_arm64=11.0

build_wheels() {
    os_platform=$1
    machine_platform=$2

    export PYTHON_OS_PLATFORM=$os_platform
    export PYTHON_MACHINE_PLATFORM=$machine_platform

    case "$os_platform" in 
        Darwin)
            version=
            if [[ "$machine_platform" == "x86_64" ]]; then
                version=$macOS_version_x86_64
            else
                version=$macOS_version_arm64
            fi

            export _PYTHON_HOST_PLATFORM="macosx-${version}-${PYTHON_MACHINE_PLATFORM}"
            ;;
        Linux)
            export _PYTHON_HOST_PLATFORM="manylinux-${glibc_version}-${PYTHON_MACHINE_PLATFORM}"
            ;;
        Windows)
            export _PYTHON_HOST_PLATFORM="win-${PYTHON_MACHINE_PLATFORM}"
            ;;
        *)
            echo "Unsupported OS: $os_platform"
            exit 1
            ;;
    esac

    pyenv exec python setup.py bdist_wheel
    rm -rf build
}

# Read the contents of the files into variables
version=$(awk -F "['\"]" '/SDK_VERSION =/{print $2}' "src/release/version.py")
build=$(awk -F "['\"]" '/SDK_BUILD_NUMBER =/{print $2}' "src/release/version.py")
release_notes=$(< src/release/RELEASE-NOTES)

# Check if Github CLI is installed
if ! command -v gh &> /dev/null; then
	echo "gh is not installed";\
	exit 1;\
fi

# Ensure GITHUB_TOKEN env var is set
if [ -z "${GITHUB_TOKEN}" ]; then
  echo "GITHUB_TOKEN environment variable is not set."
  exit 1
fi

git tag -a -s  "v${version}" -m "${version}"

# Push the tag to the branch
git push origin tag "v${version}"

gh release create "v${version}" --title "Release ${version}" --notes "${release_notes}" --repo github.com/1Password/onepassword-sdk-python


# Acquire the wheels for different OS
for version in "${python_versions[@]}"; do
pyenv local $version
build_wheels Darwin x86_64
build_wheels Darwin arm64
build_wheels Linux x86_64
build_wheels Linux aarch64
build_wheels Windows amd64
done

# Build Source as well incase wheels fails, pypi can install this as backup (standard practice)
python3 -m build --sdist

# Release on PyPi
python3 -m twine upload dist/*

# Delete the dist folder after published
rm -r dist src/*.egg-info

