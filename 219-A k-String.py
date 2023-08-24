# Brute force technique

k = int(input())
s = input()
hashset = {}
for i in s:
    if i in hashset.keys():
        hashset[i] += 1
    else:
        hashset[i] = 1
ans = ""
flag = 0
for i in hashset:
    ans += i * (hashset[i] / k)
for i in hashset:
    if hashset[i] < k:
        flag = -1
        break
if flag == 0:
    print(ans)
else:
    print(-1)


# above technique will fail after 10th test case because of following scenario
# for eg k=3
# s = "aaaaaaaaabbbbbbbbbccccccccc"
# this code will return abcabcabc
# expected return aaabbbccc
# also if k= 3
# s = "aaaabbbccc"
# output will be abcabcabc
# where due to 1 extra "c" it must return -1


k = int(input())
s = input()
hashset = {}
for i in s:
    if i in hashset.keys():
        hashset[i] += 1
    else:
        hashset[i] = 1
ans = ""
flag = 0
for i in hashset:
    ans += i * (hashset[i] // k)
for i in hashset:
    if hashset[i] < k:
        flag = -1
        break
    elif hashset[i] % k != 0:
        flag = -1
        break
if flag == 0:
    print(ans * k)
else:
    print(-1)
