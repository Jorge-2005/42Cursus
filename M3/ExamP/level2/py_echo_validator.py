def echo_validator(text: str) -> bool:
    texto: str = ""
    for c in text:
        if c.isalpha():
            texto += c
    if texto == "":
        return False
    elif texto.lower() == texto.lower()[::-1]:
        return True
    return False


print(echo_validator("333Madam ,Im A,,dam,"))
