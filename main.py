from dsl import has, isPart, set, typeclass
from rules import RuleRegistry

rules = RuleRegistry()

typeclass("W600").when(has("GEHAEUSEFORM", "S")).andWhen(isPart("K")).then(
    set("TYP", "514")
).register(rules)

rules.print()
