"""
Generated by typeshare 1.9.2
"""

from __future__ import annotations

from pydantic import BaseModel
from typing import List, Literal, Optional


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
    vault_id: str
    """
    The ID of the vault where the item is saved
    """
    fields: List[ItemField]
    """
    The item's fields
    """
    sections: List[ItemSection]
    """
    The item's sections
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
    vault_id: str
    title: str
    fields: List[ItemField]
    sections: List[ItemSection]


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
    section_id: Optional[str]
    """
    The ID of the section containing the field. Built-in fields such as usernames and passwords don't require a section.
    """
    field_type: ItemFieldType
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
    type: Literal["Otp"]
    content: OtpFieldDetails


ItemFieldDetails = ItemFieldDetailsOtp
"""
Field type-specific attributes.
"""

ItemFieldType = Literal[
    "Text", "Concealed", "CreditCardType", "Phone", "Url", "Totp", "Unsupported"
]


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
    error_message: Optional[str]
    """
    The error message, if the OTP code could not be computed
    """
