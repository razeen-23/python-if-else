j=6
for i in range(j, 0, -1):
    for k in range(j-1):
        print("  ", end="")
    for k in range(i):
        print("* ", end="")
    print()