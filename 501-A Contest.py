a = input()
lis = list(map(int, a.split()))


def findScore(points, time):
    psum = (3 * points) / 10
    tsum = points - (points / 250) * time
    return max(psum, tsum)


m = findScore(lis[0], lis[2])
v = findScore(lis[1], lis[3])
if m > v:
    print("Misha")
elif m < v:
    print("Vasya")
else:
    print("Tie")
