def cryptic_sorter(strings: list[str]) -> list[str]:

    def voc(s: str):
        return (sum(c.lower() in "aeiou" for c in s))

    words: list[str] = sorted(strings,
                              key=lambda s: (len(s), s.lower(), voc(s)))

    return words


print(cryptic_sorter(["apple", "cat", "banana", "dog", "elephant"]))
print(cryptic_sorter(["aaa", "bbb", "AAA", "BBB"]))
print(cryptic_sorter(["hello", "world", "hi", "test"]))
print(cryptic_sorter([]))
