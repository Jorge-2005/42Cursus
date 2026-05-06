from .dark_validator import dark_validate_ingredients


def dark_spell_allowed_ingredients() -> list:
    return ("bats", "frogs", "arsenic", "eyeball")


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    if dark_validate_ingredients(ingredients) == "INVALID":
        return ("rejected")
    else:
        return (f"recorded: {spell_name} "
                f"({dark_validate_ingredients(ingredients)})")
