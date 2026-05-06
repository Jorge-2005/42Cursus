def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients
    ingre: list = ingredients.split(" ")
    permited: list = light_spell_allowed_ingredients()
    for i in permited:
        for n in ingre:
            if i == n:
                return (ingredients + " - VALID")

    return ("INVALID")
