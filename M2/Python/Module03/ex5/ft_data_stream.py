from typing import Generator
import random


def gen_event() -> Generator[tuple[str, str], None, None]:
    act = ["run", "fly", "sleep", "climb", "eat", "grab", "swim", "release"]
    names = ["bob", "alice", "dylan", "charlie", "aaron", "jorge"]
    while True:
        yield (random.choice(names), random.choice(act))


def consume_event(
        event_list: list[tuple[str, str]]) -> Generator[tuple[str, str], None,
                                                        None]:
    while event_list:
        ran_index = random.randint(0, len(event_list) - 1)
        event = event_list.pop(ran_index)
        print(f"Got event from list: {event}")
        yield event


i: int = 0
gen: Generator[tuple[str, str], None, None] = gen_event()
event = next(gen)
while i <= 1000:
    print(f"Event {i}: Player {event[0]} did action {event[1]}")
    i += 1
    event = next(gen)

events_list: list[tuple[str, str]] = [next(gen) for _ in range(10)]
print(f"Built list of 10 events: {events_list}")

for event in consume_event(events_list):
    print(f"Remains in list: {events_list}")
