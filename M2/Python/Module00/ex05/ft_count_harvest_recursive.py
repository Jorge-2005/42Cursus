def helper(day, maxd):
    if day == 0:
        return
    helper(day - 1, maxd)
    print("Day", day)
    if (day == maxd):
        print("Harvest time!")


def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    helper(days, days)
