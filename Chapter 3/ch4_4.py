print(" *** Prime number summation ***")
start, stop, max_sum = input("Enter start stop max_sum : ").split()
start = int(start)
stop = int(stop)
max_sum = int(max_sum)
sum = 0
count = 0

while start <= stop and sum <= max_sum:
    ok = True
    i = 2
    if start == 1:
        ok = False
    while i < start:
        if start%i == 0:
            ok = False
            break
        i += 1

    if ok:
        if (sum+start) <= max_sum:
            count += 1
            if count == 1:
                print(f"{start}",end="")
            else:
                print(f"+{start}",end="")
            sum += start
        
    start += 1

if sum == 0:
    print("Invalid input !!!")
else:
    print(f" = {sum:,}")
    print(f"Total = {count}")
print("===== End of program =====")