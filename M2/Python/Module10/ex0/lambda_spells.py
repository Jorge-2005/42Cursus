def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    sort = sorted(artifacts, reverse=True, key=lambda x: x["power"])
    return sort


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    fil = filter(lambda x: x["power"] >= min_power, mages)
    res: list = list(fil)
    return res


def spell_transformer(spells) -> list[str]:
    mapi = map(lambda x: "*" + x["name"] + "*", spells)
    res: list = list(mapi)
    return res


def mage_stats(mages) -> dict:
    maxm: int = max(mages, key=lambda x: x["power"])["power"]
    minm: int = min(mages, key=lambda x: x["power"])["power"]

    sumn: int = sum(map(lambda x: x["power"], mages))
    rou: float = round(sumn / len(mages), 2)

    dic: dict = {"MAX": maxm, "MIN": minm, "AVERAGE": rou}
    return dic


si: list[dict] = [
    {"name": "jorge", "power": 2, "type": "ns"},
    {"name": "mauricio", "power": 9, "type": "iss"},
    {"name": "paca", "power": 1, "type": "agua"}
]

# print(artifact_sorter(si))
# print(power_filter(si, 2))
# print(spell_transformer(si))
# print(mage_stats(si))
