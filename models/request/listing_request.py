from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ListingRequest:
    request: dict
    aids: list[int] = field(init=False, default_factory=list)
    city: str = field(init=False, default=None)
    description: Optional[str] = field(init=False, default=None)
    district: Optional[str] = field(init=False, default=None)
    address: Optional[str] = field(init=False, default=None)
    phone: Optional[str] = field(init=False, default=None)

    def __post_init__(self):
        self.aids = self.request.get("aids")
        self.city = self.request.get("city")
        self.description = self.request.get("description")
        self.district = self.request.get("district")
        self.address = self.request.get("address")
        self.phone = self.request.get("phone")

    def to_dict(self):
        return {
            "aids": self.aids,
            "city": self.city,
            "description": self.description,
            "district": self.district,
            "address": self.address,
            "phone": self.phone
        }
