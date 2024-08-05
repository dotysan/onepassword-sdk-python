"""
Generated by typeshare 1.10.0-beta.7
"""

from __future__ import annotations

from pydantic import BaseModel, Field
from typing import Annotated, List, Literal, Optional


class Item(BaseModel):
    """
    Represents a 1Password item.
    """

    id: str
    """
    The item's ID
    """
    title: str
    """
    The item's title
    """
    category: ItemCategory
    """
    The item's category
    """
    vault_id: Annotated[str, Field(serialization_alias="vaultId")]
    """
    The ID of the vault where the item is saved
    """
    tags: List[str]
    """
    The item's tags
    """
    fields: List[ItemField]
    """
    The item's fields
    """
    sections: List[ItemSection]
    """
    The item's sections
    """
    version: int
    """
    The item's version
    """


ItemCategory = Literal[
    "Login",
    "SecureNote",
    "CreditCard",
    "CryptoWallet",
    "Identity",
    "Password",
    "Document",
    "ApiCredentials",
    "BankAccount",
    "Database",
    "DriverLicense",
    "Email",
    "MedicalRecord",
    "Membership",
    "OutdoorLicense",
    "Passport",
    "Rewards",
    "Router",
    "Server",
    "SshKey",
    "SocialSecurityNumber",
    "SoftwareLicense",
    "Person",
    "Unsupported",
]


class ItemCreateParams(BaseModel):
    category: ItemCategory
    """
    The item's category
    """
    vault_id: Annotated[str, Field(serialization_alias="vaultId")]
    """
    The ID of the vault where the item is saved
    """
    title: str
    """
    The item's title
    """
    fields: List[ItemField]
    """
    The item's fields
    """
    sections: List[ItemSection]
    """
    The item's sections
    """
    tags: List[str]
    """
    The item's tags
    """


class ItemField(BaseModel):
    """
    Represents a field within an item.
    """

    id: str
    """
    The field's ID
    """
    title: str
    """
    The field's title
    """
    section_id: Annotated[Optional[str], Field(serialization_alias="sectionId")]
    """
    The ID of the section containing the field. Built-in fields such as usernames and passwords don't require a section.
    """
    field_type: Annotated[ItemFieldType, Field(serialization_alias="fieldType")]
    """
    The field's type
    """
    value: str
    """
    The string representation of the field's value
    """
    details: Optional[ItemFieldDetails]
    """
    Field type-specific attributes.
    """


class ItemFieldDetailsOtp(BaseModel):
    type: Literal["otp"]
    content: OtpFieldDetails


ItemFieldDetails = ItemFieldDetailsOtp
"""
Field type-specific attributes.
"""

ItemFieldType = Literal[
    "Text", "Concealed", "CreditCardType", "Phone", "Url", "Totp", "Unsupported"
]


class ItemOverview(BaseModel):
    """
    Represents a decrypted 1Password item.
    """

    id: str
    """
    The item's ID
    """
    title: str
    """
    The item's title
    """
    category: ItemCategory
    """
    The item's category
    """
    vault_id: Annotated[str, Field(serialization_alias="vaultId")]
    """
    The ID of the vault where the item is saved
    """


class ItemSection(BaseModel):
    """
    A section groups together multiple fields in an item.
    """

    id: str
    """
    The section's unique ID
    """
    title: str
    """
    The section's title
    """


class OtpFieldDetails(BaseModel):
    """
    Additional attributes for OTP fields.
    """

    code: Optional[str]
    """
    The OTP code, if successfully computed
    """
    error_message: Annotated[Optional[str], Field(serialization_alias="errorMessage")]
    """
    The error message, if the OTP code could not be computed
    """


class VaultOverview(BaseModel):
    """
    Represents a decrypted 1Password vault.
    """

    id: str
    """
    The vault's ID
    """
    title: str
    """
    The vault's title
    """
