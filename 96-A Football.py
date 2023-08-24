str1 = input()
prev = str1[0]
count = 1
flag = False
for i in range(len(str1)):
    if str1[i] != prev:
        count = 1
    if count == 7:
        flag = True
    count += 1
    prev = str1[i]
if flag:
    print("YES")
else:
    print("NO")
