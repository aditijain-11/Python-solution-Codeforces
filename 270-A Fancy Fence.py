# very easy question

n = int(input())
lis = []
for i in range(n):
    angle = int(input())
    lis.append(angle)
for i in lis:
    x = 360 / (180 - i)
    if x == int(x):
        print("YES")
    else:
        print("NO")
