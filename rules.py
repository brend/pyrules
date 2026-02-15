from __future__ import annotations

from collections import defaultdict

from actions import Action
from conditions import Condition
from product import Product


class Rule:
    def __init__(
        self, typeclass: str, conditions: list[Condition], actions: list[Action]
    ) -> None:
        self.typeclass = typeclass
        self.conditions = conditions
        self.actions = actions
        super().__init__()

    def apply(self, product: Product) -> None:
        if self.is_applicable(product):
            self.apply_actions(product)

    def is_applicable(self, product: Product) -> bool:
        for condition in self.conditions:
            if not condition.matches(product):
                return False
        return True

    def apply_actions(self, product: Product) -> None:
        for action in self.actions:
            action.apply(product)

    def __repr__(self) -> str:
        conds = " and ".join(str(c) for c in self.conditions)
        acts = " and ".join(str(a) for a in self.actions)
        return f"if {conds} then {acts}"


class RuleRegistry:
    def __init__(self) -> None:
        self.classRules: dict[str, list[Rule]] = defaultdict(list)

    def register(self, rule: Rule):
        self.classRules[rule.typeclass].append(rule)

    def apply(self, product: Product) -> None:
        for rule in self.classRules[product.typeclass]:
            rule.apply(product)

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
