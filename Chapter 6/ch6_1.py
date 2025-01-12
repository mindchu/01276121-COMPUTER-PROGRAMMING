print(" *** Sum odd / Subtract even ***")
num = input("Enter numbers : ").split()
sum = 0
for i in num:
    i = int(i)
    if i % 2 == 0:
        sum -= i
    else:
        sum += i
print("Sum is",sum)