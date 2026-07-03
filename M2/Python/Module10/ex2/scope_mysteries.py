from typing import Callable
from typing import Any


def mage_counter() -> Callable:
    count: int = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    count: int = initial_power

    def add(more: int) -> int:
        nonlocal count
        count += more
        return count
    return add


def enchantment_factory(enchantment_type: str) -> Callable:
    item: str = enchantment_type

    def des(description) -> str:
        news: str = f"{item} {description}"
        return news
    return des


def memory_vault() -> dict[str, Callable]:
    dicti: dict[str, Callable] = {}

    def store(key, value) -> None:
        dicti[key] = value

    def recall(key) -> Any:
        for k, value in dicti.items():
            if k == key:
                return value
        return "Memory not found"
    return {"store": store, "recall": recall}


"""
ho = mage_counter()
ho()
ho()
lol = mage_counter()

ad = spell_accumulator(2)

items = enchantment_factory("espada")

loc = memory_vault()
loc["store"]("nombre", 32)
print(loc["recall"]("nombre"))
"""
