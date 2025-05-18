J = 'ab'.strip()
S = 'aabbccd'.strip()
res = 0
jset = set(J)
for i in S:
    if i in jset:
        res += 1
print(res)