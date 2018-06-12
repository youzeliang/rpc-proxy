L = list(range(100))

print(L[:10])

q = (x * x for x in range(1, 10) if x == 2)
for a in q:
    print(a)