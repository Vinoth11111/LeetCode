a = 'the sky is blue'
b = a.split()
rev_word = ''
for i in b[::-1]:
   rev_word += str(i) + ' '
print(rev_word)
