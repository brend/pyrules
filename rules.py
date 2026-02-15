from __future__ import annotations

from abc import ABC, abstractmethod
from collections import defaultdict


class Product:
    def __init__(self, part: str) -> None:
        self.part = part
        self.attributes: dict[str, str] = defaultdict(None)

    def get(self, attribute: str) -> str | None:
        self.attributes[attribute]

    def set(self, attribute: str, value: str) -> None:
        self.attributes[attribute] = value


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


class Rule(ABC):
    def __init__(
        self, typeclass: str, conditions: list[Condition], actions: list[Action]
    ) -> None:
        self.typeclass = typeclass
        self.conditions = conditions
        self.actions = actions
        super().__init__()

    def __repr__(self) -> str:
        conds = " and ".join(str(c) for c in self.conditions)
        acts = " and ".join(str(a) for a in self.actions)
        return f"if {conds} then {acts}"


class RuleRegistry:
    def __init__(self) -> None:
        self.classRules: dict[str, list[Rule]] = defaultdict(list)

    def register(self, rule: Rule):
        self.classRules[rule.typeclass].append(rule)

    def print(self) -> None:
        for typeclass, rules in self.classRules.items():
            print("class", typeclass)
            for rule in rules:
                print("  ", rule)


class TypeclassRuleBuilder:
    def __init__(self, typeclass: str) -> None:
        self.typeclass = typeclass

    def when(self, condition: Condition) -> ConditionRuleBuilder:
        return ConditionRuleBuilder(self.typeclass, [condition])

    def then(self, action: Action) -> ActionRuleBuilder:
        return ActionRuleBuilder(self.typeclass, [], [action])


class ConditionRuleBuilder:
    def __init__(self, typeclass: str, conditions: list[Condition] = []) -> None:
        self.typeclass = typeclass
        self.conditions = conditions

    def and_when(self, condition: Condition) -> ConditionRuleBuilder:
        self.conditions.append(condition)
        return self

    def then(self, action: Action) -> ActionRuleBuilder:
        return ActionRuleBuilder(self.typeclass, self.conditions, [action])


class ActionRuleBuilder:
    def __init__(
        self,
        typeclass: str,
        conditions: list[Condition] = [],
        actions: list[Action] = [],
    ) -> None:
        self.typeclass = typeclass
        self.conditions = conditions
        self.actions = actions

    def andThen(self, action: Action) -> ActionRuleBuilder:
        self.actions.append(action)
        return self

    def compile(self) -> Rule:
        return Rule(self.typeclass, self.conditions, self.actions)

    def register(self, registry: RuleRegistry) -> None:
        registry.register(self.compile())
