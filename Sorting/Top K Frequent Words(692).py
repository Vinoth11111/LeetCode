# https://leetcode.com/problems/top-k-frequent-words/
from collections import Counter


def sol(words, k):
    has = Counter(words)
    sorted_word = sorted(has, key=lambda x: (-has[x], x))
    return sorted_word[:k]


print(sol(["i", "love", "leetcode", "i", "love", "coding"], 3))
print(sol(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4))
