mark = int(input("enter your marks:"))
if mark>= 90 and mark<=100:
    print("A grade")
elif mark>= 75 and mark<=89:
    print("b grade")
elif mark>= 60 and mark<=74:
    print("c grade")
elif mark>= 40 and mark<=59:
    print("d grade")
else:
    print("FAIL")