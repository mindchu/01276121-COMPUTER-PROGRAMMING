print(" *** Butterfly ***")
num = int(input("Input a positive integer : "))
ok = False
if num > 0:
    ok = True

upper_row = 0
space = (2*num)-2
if ok:
    print()
    for upper_row in range(num):
        star = upper_row + 1
        print(f"{'*'*star}{' '*space}{'*'*star}")
        upper_row += 1
        space -= 2
    if num > 1:
        space = 0
        for lower_row in range(num-1):
            star = upper_row - 1
            space += 2
            print(f"{'*'*star}{' '*space}{'*'*star}")
            upper_row -= 1
    print()
else:
    print("!!!Please enter positive number!!!")

print("===== End of program =====")