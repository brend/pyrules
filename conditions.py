from abc import ABC, abstractmethod

from product import Product


class Condition(ABC):
    @abstractmethod
    def matches(self, product: Product) -> bool:
        pass


class Has(Condition):
    def __init__(self, attribute: str, value: str) -> None:
        super().__init__()
        self.attribute = attribute
        self.value = value

    def matches(self, product: Product) -> bool:
        return product.get(self.attribute) == self.value

    def __str__(self) -> str:
        return f"{self.attribute} is {self.value}"


class IsPart(Condition):
    def __init__(self, part: str) -> None:
        super().__init__()
        self.part = part

    def matches(self, product: Product) -> bool:
        return product.part == self.part

    def __str__(self) -> str:
        return f"it is a {self.part}"
