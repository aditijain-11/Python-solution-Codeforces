n = int(input())
lis = input()
lis = list(map(int, lis.split()))
res = []
for i in range(n):
    for j in range(n):
        if lis[j] == i + 1:
            res.append(j + 1)
            break
ans = " ".join(map(str, res))
print(ans)
