from collections import Counter


def compare_strings(my_strings: str) -> str:
    counter = Counter(my_strings)
    haeufigstes_zeichen = counter.most_common(1)[0][0]
    anzahl = counter.most_common(1)[0][1]
    return (f"Häufigstes Zeichen: {haeufigstes_zeichen},"
            f"Anzahl: {anzahl},"
            f"an der Position: {my_strings.index(haeufigstes_zeichen)}"
)


string = "aaabbbccccdddddeeeee"
result = compare_strings(string)
print(result)
