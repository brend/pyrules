from collections import defaultdict
from typing import Optional


class Product:
    def __init__(
        self, typeclass: str, part: str, attributes: dict[str, str] = {}
    ) -> None:
        self.typeclass = typeclass
        self.part = part
        self.attributes: dict[str, str] = defaultdict(None)
        for key, value in attributes.items():
            self.attributes[key] = value

    def get(self, attribute: str) -> Optional[str]:
        return self.attributes[attribute]

    def set(self, attribute: str, value: str) -> None:
        self.attributes[attribute] = value

    def __str__(self):
        return f"Product({self.typeclass}, {self.part}, {self.attributes})"
