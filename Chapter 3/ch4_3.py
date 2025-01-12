print(" *** Fibonacci sequence ***")
a0,a1,n = input("Enter a0 a1 n : ").split()
a0 = int(a0)
a1 = int(a1)
n = int(n)
i = 0
while i < n:
    if i == 0:
        print(f"{a0}, ",end="")
    elif i == 1:
        print(f"{a1}, ",end="")
    else:
        sum = a0 + a1
        if i == (n-1):
            print(f"{sum}")
        else:
            print(f"{sum}, ",end="")
        a0, a1 = a1, sum
    i += 1
print("===== End of program =====")