n, m = map(int, input().split(" "))
lis_a = list(map(int, input().split()))
count = lis_a[0] - 1
for i in range(1, m):
    if lis_a[i - 1] > lis_a[i]:
        count += n - (lis_a[i - 1] - lis_a[i])
    else:
        count += lis_a[i] - lis_a[i - 1]
print(count)
