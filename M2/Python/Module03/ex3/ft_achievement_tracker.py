import random


def gen_player_achievements() -> set[str]:
    ach = ['Crafting Genius', 'Strategist', 'World Savior', 'Speed Runner',
           'Survivor', 'Master Explorer', 'Treasure Hunter', 'Unstoppable',
           'First Steps', 'Collector Supreme', 'Untouchable', 'Sharp Mind',
           'Boss Slayer']

    return set(random.sample(ach, random.randint(1, 13)))


def all_achievements() -> set[str]:
    ach = {'Crafting Genius', 'Strategist', 'World Savior', 'Speed Runner',
           'Survivor', 'Master Explorer', 'Treasure Hunter', 'Unstoppable',
           'First Steps', 'Collector Supreme', 'Untouchable', 'Sharp Mind',
           'Boss Slayer'}

    return ach


print("=== Achievement Tracker System ===\n")
player1 = gen_player_achievements()
player2 = gen_player_achievements()
player3 = gen_player_achievements()
player4 = gen_player_achievements()
# imprime los personajes
print(f"Player Alice: {player1}")
print(f"Player Bob: {player2}")
print(f"Player Charlie: {player3}")
print(f"Player Dylan: {player4}\n")
# junta todos los elemntos sin repetir
print(f"All distinct achievements: {player1 | player2 | player3 | player4}\n")
# imprime solo los elementos que estan en todos
print(f"Common achievements: {player1 & player2 & player3 & player4}\n")
# imprime los elementos que estan en uno pero no en otro
print(f"Only Alice has: {player1 - player2 - player3 - player4}")
print(f"Only Bob has: {player2 - player1 - player3 - player4}")
print(f"Only Charlie has: {player3 - player1 - player2 - player4}")
print(f"Only Dylan has: {player4 - player1 - player2 - player3}\n")

achievements = all_achievements()
print(f"Alice is missing: {achievements - player1}")
print(f"Bob is missing: {achievements - player2}")
print(f"Charlie is missing: {achievements - player3}")
print(f"Dylan is missing: {achievements - player4}")
