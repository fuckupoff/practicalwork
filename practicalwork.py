J = 'ab'
S = 'aabbccd'
res = 0
jset = set(J)
for i in S:
    if i in jset:
        res += 1
print(res)
