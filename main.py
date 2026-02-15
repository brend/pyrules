from dsl import has, is_part, set, typeclass
from rules import RuleRegistry

rules = RuleRegistry()

typeclass("W600").when(has("GEHAEUSEFORM", "S")).and_when(is_part("K")).then(
    set("TYP", "514")
).register(rules)

rules.print()
