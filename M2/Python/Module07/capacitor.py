from ex1 import HealingCreatureFactory, TransformCreatureFactory


hola = HealingCreatureFactory().create_base()
adios = HealingCreatureFactory().create_evolved()

hola2 = TransformCreatureFactory().create_base()
adios2 = TransformCreatureFactory().create_evolved()

print("Testing Creature with healing capability \n base:")

print(hola.describe())
print(hola.attack())
print(hola.heal())  # type: ignore

print(" evolved:")

print(adios.describe())
print(adios.attack())
print(adios.heal())  # type: ignore

print("\nTesting Creature with transform capability\n base:")
print(hola2.describe())
print(hola2.attack())
print(hola2.transform())  # type: ignore
print("Shiftling performs a boosted strike!")
print(hola2.revert())  # type: ignore

print(" evolved:")

print(adios2.describe())
print(adios2.attack())
print(adios2.transform())  # type: ignore
print("Morphagon unleashes a devastating morph strike!")
print(adios2.revert())  # type: ignore
