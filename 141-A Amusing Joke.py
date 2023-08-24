if __name__ == "__main__":
    name = input() + input()
    pile = input()
    if len(name) != len(pile):
        print("NO")
        exit()
    else:
        for c in name:
            if name.count(c) != pile.count(c):
                print("NO")
                exit()
    print("YES")
