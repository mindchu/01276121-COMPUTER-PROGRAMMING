print(" *** 3-digit number ***")
num = int(input("Enter 3-digit number : "))
first = num//100
second = num//10%10
third = num%10
# print(first,second,third)
if first % 2 == 0:
    digit_1 = "Even"
else:
    digit_1 = "Odd"
if second % 2 == 0:
    digit_2 = "Even"
else:
    digit_2 = "Odd"
if third % 2 == 0:
    digit_3 = "Even"
else:
    digit_3 = "Odd"

print(f"{num} => {digit_1} {digit_2} {digit_3}")

value = (first**2)+(second**3)+(third**4)

print(f"{first}^2 + {second}^3 + {third}^4 = {value:,}")
print("===== End of program =====")