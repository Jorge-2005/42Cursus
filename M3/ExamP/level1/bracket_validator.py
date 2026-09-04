def bracket_validator(s: str) -> bool:
    stack = []
    valid = {"(": ")", "[": "]", "{": "}"}

    for c in s:
        if c in valid:
            stack.append(c)
        elif c in valid.values():
            if not stack:
                return False
            elif valid[stack[-1]] != c:
                return False
            stack.pop()

    if not stack:
        return True
    return False


# print(bracket_validator("hola(("))
print(bracket_validator(""))
