from functools import wraps
from typing import Callable, Any
import time


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}")
        start = time.perf_counter()
        res = func(*args, **kwargs)
        end = time.perf_counter()
        total_t = end - start
        print(f"Spell completed in {total_t:.3f} seconds")
        return res
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            if "power" in kwargs:
                power = kwargs["power"]
            elif len(args) >= 3:
                power = args[2]
            else:
                power = args[0]

            if power >= min_power:
                return func(*args, **kwargs)

            return "Insufficient power for this spell"

        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)

                except Exception:
                    if attempt < max_attempts:
                        print(f"Spell failed, retrying..."
                              f"(attempt {attempt}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        return name.replace(" ", "").isalpha()

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    @spell_timer
    def s_timer():
        i: int = 0
        while i < 100000000:
            i += 1
        print(i)

    @power_validator(50)
    def fireball(power):
        return f"Fireball cast with power {power}"

    @retry_spell(3)
    def dividir():
        i = 10 / 0
        print(i)

    # classg = MageGuild()
    # print(classg.cast_spell("Lightning", 15))
    # print(classg.cast_spell("lol", 7))
    # print(dividir(0))
    # s_timer()
    # print(fireball(50))
