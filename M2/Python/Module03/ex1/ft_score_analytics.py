import sys

print("=== Player Score Analytics ===")
if (len(sys.argv) == 1):
    print("No scores provided. Usage: python3 ft_score_analytics.py ...")
else:
    length: int = len(sys.argv)
    i: int = 1
    total_players: int = 0
    average_score: int = 0
    high_score: int = 0
    low_score: int = 0
    while (i < length):
        try:
            average_score += int(sys.argv[i])
            total_players += 1
            if (int(sys.argv[i]) > high_score):
                high_score = int(sys.argv[i])
            if (total_players == 1):
                low_score = int(sys.argv[i])
            if (int(sys.argv[i]) < low_score):
                low_score = int(sys.argv[i])
        except ValueError:
            print(f"Invalid parameter: '{sys.argv[i]}'")
        i += 1


def scores() -> list:
    lista: list = sys.argv
    i = 1
    j = 0
    while (i < length):
        try:
            lista[j] = int(sys.argv[i])
            i += 1
            j += 1
        except ValueError:
            i += 1
    return lista


if (len(sys.argv) != 1):
    if (total_players != 0):
        new_list = scores()
        print(f"Scores processed: {new_list[: -(length - total_players)]}")
        print(f"Total players: {total_players}")
        print(f"Total score: {average_score}")
        print(f"Average score: {average_score / total_players}")
        print(f"High score: {high_score}")
        print(f"Low score: {low_score}")
        print(f"Score range: {high_score - low_score}")
    else:
        print("No scores provided. Usage: python3 ft_score_analytics.py ...")
