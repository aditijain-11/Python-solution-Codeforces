n = int(input())
p = input()
py = [0]
py.extend(list(map(int, p.split())))
e = d = 0
type(py[1])
for i in range(1, n + 1):
    e += py[i - 1] - py[i]
    if e < 0:
        d -= e
        e = 0
print(d)
