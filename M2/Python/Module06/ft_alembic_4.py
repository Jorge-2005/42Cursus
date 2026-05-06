import alchemy

print(alchemy.create_air())

try:
    print(alchemy.create_earth())

except AttributeError:
    print("\nFunction not availabe")
