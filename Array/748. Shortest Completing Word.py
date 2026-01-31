# https://leetcode.com/problems/shortest-completing-word/?envType=problem-list-v2&envId=string
def sol(license_plate, word):
    lp_char = []
    for i in license_plate:
        if i.isalpha():
            lp_char.append(i.lower())
    res = ''
    for i in word:
        temp = list(i)
        valid = True
        for j in lp_char:
            if j in temp:
                temp.remove(j)
            else:
                valid = False
                break
        if valid:
            if res == '' or len(res) > len(i):
                res = i
    return res


print(sol("1s3 PSt", ["step", "steps", "stripe", "stepple"]))
print(sol("1s3 456", ["looks", "pest", "stew", "show"]))
