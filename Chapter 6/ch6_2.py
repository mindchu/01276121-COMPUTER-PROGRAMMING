print(" *** Reverse Even ***")
num = input("Enter integers : ").split()
num = [int(i) for i in num]
print(num)
reverse_num = []
for i in num[::-1]:
    if i % 2 == 0:
        reverse_num.append(i)
result = []
count = 0
for i in num:
    if i % 2 == 0:
        result.append(reverse_num[count])
        count += 1
    else:
        result.append(i)
print(result)
print("===== End of program =====")
