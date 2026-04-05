import sys

print("=== Inventory System Analysis ===")
items_list: list[str] = ["sword", "potion", "shield", "armor", "helmet",
                         "magic_item"]
check: list[str] = []
value: int = 0
inventory: dict[str, int] = {}
for palabra in sys.argv[1:]:
    if ":" not in palabra:
        print(f"Error - invalid parameter '{palabra}'")
    else:
        item: list[str] = palabra.split(":")
        if len(item) == 2:
            if item[0] in items_list:
                if item[0] in check:
                    print(f"Redundant item '{item[0]}' - discarding")
                else:
                    try:
                        value = int(item[1])
                        check.append(item[0])
                        inventory[item[0]] = value
                    except ValueError as e:
                        print(f"Quantity error for '{item[0]}': {e}")
            else:
                print(f"Error - not an item: '{palabra}'")
        else:
            print(f"Error - invalid parameter: '{palabra}'")

print(f"Got inventory: {inventory}")
print(f"Item list: {check}")

value = 0
for k in inventory.values():
    value += k
print(f"Total quantity of the {len(check)} items: {value}")

for part, number in inventory.items():
    percent = (number / value) * 100
    print(f"Item {part} represents {percent}%")

max: int = 0
min: int = 0
max_item: str = ""
min_item: str = ""
i = 0
for part, number in inventory.items():
    if i == 0:
        max = number
        min = number
        min_item = part
        max_item = part
    if number > max:
        max = number
        max_item = part
    if number < min:
        min = number
        min_item = part
    i += 1
print(f"Item most abundant: {max_item} with quantity {max}")
print(f"Item least abundant: {min_item} with quantity {min}")
inventory["magic_item"] = 1
print(f"Updated inventory: {inventory}")
