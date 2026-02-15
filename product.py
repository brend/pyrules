from collections import defaultdict
from typing import Optional


class Product:
    def __init__(self, part: str) -> None:
        self.part = part
        self.attributes: dict[str, str] = defaultdict(None)

    def get(self, attribute: str) -> Optional[str]:
        self.attributes[attribute]

    def set(self, attribute: str, value: str) -> None:
        self.attributes[attribute] = value
