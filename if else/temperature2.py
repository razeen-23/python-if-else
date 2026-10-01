temp = int(input("enter the temperature:"))
if temp<15:
    print("cold")
elif temp>= 15 and temp<=30:
    print("normal")
elif temp>= 31 and temp<=40:
    print("Hot")
else:
    print("Very  Hot")
