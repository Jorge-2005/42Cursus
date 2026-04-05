import random


names: list[str] = ["bob", "Alice", "dylan", "charlie", "Aaron", "Jorge",
                    "Liam", "emma"]

print("=== Game Data Alchemist ===\n")
print(f"Initial list of players: {names}")
all_cap: list[str] = [i.capitalize() for i in names]
print(f"New list with all names capitalized: {all_cap}")
cap_names: list[str] = [i for i in names if i == i.capitalize()]
print(f"New list of capitalized names only: {cap_names}\n")

score_dict: dict[str, int] = {name: random.randint(0, 999) for name in all_cap}
print(f"Score dict: {score_dict}")
av_score: int = round(sum(score_dict.values()) / len(names))
print(f"Score average is {av_score}")
high_score_dict: dict[str, int] = {name: num for name, num in
                                   score_dict.items() if num > av_score}
print(f"High scores: {high_score_dict}")
