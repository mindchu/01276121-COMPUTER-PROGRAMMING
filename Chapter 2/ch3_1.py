print(" *** Number Manipulation ***")
num = int(input("Enter a whole number : "))
if num % 2 == 0:
    print(num,"is even.")
else:
    print(num,"is odd.")
if num < 0:
    print(f"absolute value of {num} ==> {num * -1}")
else:
    print(f"absolute value of {num} ==> {num}")