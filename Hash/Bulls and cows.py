# https://leetcode.com/problems/bulls-and-cows/?envType=problem-list-v2&envId=hash-table

def sol(secret, guess):
    s_has = {}
    # g_has = {}
    # res = '0A0B'
    cur_gus = 0
    wr_ind = 0
    check_ind = []
    for i in range(len(secret)):
        if secret[i] == guess[i]:
            cur_gus += 1
            check_ind.append(i)
        elif secret[i] not in s_has:
            s_has[secret[i]] = 1
        else:
            s_has[secret[i]] += 1
    for i in range(len(guess)):
        if guess[i] in s_has and s_has[guess[i]] != 0 and i not in check_ind:
            s_has[guess[i]] = s_has[guess[i]] - 1
            wr_ind += 1

    return f'{cur_gus}A{wr_ind}B'


print(sol("1807", "7810"))
print(sol("1123", "0111"))
print(sol('10', '11'))
