if __name__ == "__main__":
    times = int(input())
    ans = []
    for i in range(times):
        w = input()
        if (len(w)) > 10:
            s = w[0] + str(len(w) - 2) + w[-1]
            ans.append(s)
        else:
            ans.append(w)
    for ch in ans:
        print(ch)
