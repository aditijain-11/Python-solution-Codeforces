n, k = map(int, input().split(" "))
perms = [0] * n
value = n
for i in range(n - 1, k, -1):
    perms[i] = value
    value -= 1
for i in range(0, k + 1):
    perms[i] = value
    value -= 1

ans = " ".join(map(str, perms))
print(ans)
