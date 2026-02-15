from abc import ABC, abstractmethod

from product import Product


class Action(ABC):
    @abstractmethod
    def apply(self, product: Product) -> None:
        pass


class Set(Action):
    def __init__(self, attribute: str, value: str) -> None:
        super().__init__()
        self.attribute = attribute
        self.value = value

    def apply(self, product: Product) -> None:
        product.set(self.attribute, self.value)

    def __str__(self) -> str:
        return f"set {self.attribute} to {self.value}"
