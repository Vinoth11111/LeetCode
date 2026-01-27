# https://leetcode.com/problems/word-pattern/?envType=problem-list-v2&envId=string
def wordPattern(pattern, s):
    p_has = {}
    s_has = {}

    for ind, p in enumerate(pattern):
        if p not in p_has:
            p_has[p] = ind
        else:
            p_has[p] += ind
    for ind, st in enumerate(s.split()):
        if st not in s_has:
            s_has[st] = ind
        else:
            s_has[st] += ind

    if len(s_has) != len(p_has):
        return False
    else:
        for s_val, p_val in zip(s_has, p_has):
            if s_has[s_val] != p_has[p_val]:
                return False
    return True


print(wordPattern("abba", "dog cat cat dog"))
print(wordPattern("aba", "cat cat cat dog"))


# pattern 2: use the word matching.
"""
def wordPattern(pattern: str, s: str) -> bool:
    words = s.split()  # Split the string into words
    if len(pattern) != len(words):
        return False

    # Dictionaries to store character-to-word and word-to-character mappings
    char_to_word = {}
    word_to_char = {}

    for p, w in zip(pattern, words):
        # If the pattern character has been mapped before, check the word mapping
        if p in char_to_word:
            if char_to_word[p] != w:
                return False
        else:
            char_to_word[p] = w

        # If the word has been mapped to a different pattern character, return False
        if w in word_to_char:
            if word_to_char[w] != p:
                return False
        else:
            word_to_char[w] = p

    return True
"""
