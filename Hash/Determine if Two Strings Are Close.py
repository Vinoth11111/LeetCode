# https://leetcode.com/problems/determine-if-two-strings-are-close/solutions/7427760/determine-if-two-strings-are-close-by-vi-ki4t/

def sol(word1, word2):
    if len(word1) != len(word2) or set(word1) != set(word2):
        return False
    has1 = {}
    has2 = {}
    for i, j in zip(word1, word2):
        has1[i] = has1.get(i, 0) + 1
        has2[j] = has2.get(j, 0) + 1
    if sorted(has1.values()) == sorted(has2.values()):
        return True
    return False


print(sol("abc", "bca"))
print(sol("cabbba", "aabbss"))
print(sol("abbzzca", "babzzcz"))
