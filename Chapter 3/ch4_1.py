print(" *** odd integer summation from 1 to n ***")
num = int(input("Enter an integer(n) : "))
ok = True
if num <= 0:
    print(f"The input [{num}] must be greater than or equal to 1 !!!]")
    ok = False
i = 1
sum = 0
if ok :
    print(f"Summation => ",end="")
    while i <= num :
        if i % 2 != 0 :
            if i == (num-1) or i == num:
                print(i,end="")
                sum += i
            else :
                print(f"{i}+",end="")
                sum += i
        i += 1
    print(f" = {sum}")
print("===== End of program ======")