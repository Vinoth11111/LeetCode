# https://leetcode.com/problems/reorder-data-in-log-files/description/
def sol(logs):
    letter = []
    digit = []

    for log in logs:
        part = log.split()
        identifier = part[0]
        content = part[1:]
        if content[0].isdigit():
            digit.append(log)
        else:
            letter.append((content, identifier))

    letter.sort(key=lambda x: (x[0], x[1]))
    final_letter = [f"{idn} {' '.join(con)}" for con, idn in letter]
    return final_letter + digit


print(sol(["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]))  # ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
print(sol(["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]))  # ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
