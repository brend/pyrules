from rules import Has, IsPart, Set, TypeclassRuleBuilder


def typeclass(typeclass: str) -> TypeclassRuleBuilder:
    return TypeclassRuleBuilder(typeclass)


def has(attribute: str, value: str) -> Has:
    return Has(attribute, value)


def is_part(part: str) -> IsPart:
    return IsPart(part)


def set(attribute: str, value: str) -> Set:
    return Set(attribute, value)
