from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul
from typing import Callable
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    else:
        if operation == "add":
            return reduce(add, spells)
        elif operation == "multiply":
            return reduce(mul, spells)
        elif operation == "max":
            return reduce(max, spells)
        elif operation == "min":
            return reduce(min, spells)
        else:
            return 0


"""
def base_enchantment(name, power, element):
    return f"{element} spell hits {name} with power {power}"
"""


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    fire = partial(base_enchantment, power=50, element="fire")
    ice = partial(base_enchantment, power=50, element="ice")
    light = partial(base_enchantment, power=50, element="light")

    return {"fire": fire, "ice": ice, "light": light}


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return memoized_fibonacci(n-1) + memoized_fibonacci(n-2)


def spell_dispatcher() -> Callable[[Any], str]:

    @singledispatch
    def dispatcher(spell: Any) -> str:
        return "unknown type"

    @dispatcher.register(int)
    def _(spell: int) -> str:
        return f"damage: {spell}"

    @dispatcher.register(str)
    def _(spell: str) -> str:
        return f"enchant: {spell}"

    @dispatcher.register(list)
    def _(spell: list) -> str:
        return f"multi: {len(spell)} spells"

    return dispatcher


# hi = spell_reducer([2, 4, 6], "min")
# print(hi)

# lol = partial_enchanter(base_enchantment)
# print(lol["fire"]("orc"))
# print(lol["ice"]("dragon"))
# print(lol["light"]("goblin"))

# print(memoized_fibonacci(499))

# spell = spell_dispatcher()
# print(spell(2))
# print(spell("fire"))
# print(spell([1, "lol", 2]))
