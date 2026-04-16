def cryptic_sort(strings: list[str]) -> list[str]:
    return sorted(strings, key=lambda s: (len(s), s.lower(), sum(c in "aeiouAEIOU" for c in s)))

# Example
print(cryptic_sort(["A", "banana", "grape", "kiwi", "oArange"]))
print(cryptic_sort(["a", "e", "b", "o", "u"]))
print(cryptic_sort(["Arsen", "arsen", "ARSEN"]))
print(cryptic_sort(["aaa", "AAA", "bbb", "BBB"]))




### Test ###

print(cryptic_sorter([""]))
words = ["bat", "cat", "ant"]
print(cryptic_sorter(words)) 
# ["sky", "rhythm", "test", "Apple", "aeiou"]
print(cryptic_sorter(["BBB", "bbb", "ccc", "CCC"]))
