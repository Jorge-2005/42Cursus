from typing import Callable


def spell(target: str, power: int) -> str:
    return (f"Spell to {target} and use {power} of power")


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    if callable(spell1) and callable(spell2):
        def combined(target: str, power: int) -> tuple:
            return (spell1(target, power), spell2(target, power))

        return combined
    else:
        print("not a function")


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    if callable(base_spell):
        def multi(target: str, power: int) -> str:
            return base_spell(target, power * multiplier)

        return multi


"""
def condition(target: str, power: int) -> bool:
    return power > 50
"""


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def new_spell(target: str, power: int):
        if condition(target, power):
            return spell(target, power)
        else:
            return "Spell fizzled"

    return new_spell


def spell_sequence(spells: list[Callable]) -> Callable:
    def spell_list(target: str, power: int) -> list:
        slist: list = []
        for spel in spells:
            slist.append(spel(target, power))
        return slist
    return spell_list


# si = [spell, spell, spell]
# combined = spell_combiner(spell, spell)
# multi = power_amplifier(spell, 2)
# cond = conditional_caster(condition, spell)
# li = spell_sequence(si)
# print(li("lol", 60))
