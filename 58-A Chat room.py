s = "hello"
s2 = input()
s2 = s2.lower()
i = 0
for j in range(len(s2)):
    if i >= len(s):
        break
    if s2[j] == s[i]:
        i += 1
if i != len(s):
    print("NO")
else:
    print("YES")
