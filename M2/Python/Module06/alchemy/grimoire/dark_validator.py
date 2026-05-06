def dark_validate_ingredients(ingredients: str) -> str:
    from .dark_spellbook import dark_spell_allowed_ingredients
    ingre: list = ingredients.split(" ")
    permited: list = dark_spell_allowed_ingredients()
    for i in permited:
        for n in ingre:
            if i == n:
                return (ingredients + " - VALID")

    return ("INVALID")
