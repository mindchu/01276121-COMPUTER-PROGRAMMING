print(" *** Binary to Decimal ***")
num = input("Enter binary number : ")
count = -1
sum = 0
binary = None
for i in num:
    if i == "$":
        break
    elif i == "0" or i == "1":
        if binary == None:
            binary = i
        else:
            binary = binary + i
        count += 1

for i in binary:
    i = int(i)
    sum += (2**count)*i
    count -= 1

print(f"{binary} ==> {sum}")
print("===== End of program ======")