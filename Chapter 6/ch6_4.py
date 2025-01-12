print(" *** Median Mean ***")
list0 = input("Enter numbers : ").split()
print(f"list0 =  {list0}")

list1 = []
list2 = []
for i in list0:
    try:
        i = float(i)
        if i % 1 == 0:
            i = int(i)
            list1.append(i)
        else:
            list1.append(i)
    except:
        list2.append(i)
print(f"list1 =  {list1}")

sum = 0
count = 0
for i in list1:
    sum += i
    count += 1
Mean = sum/count
if Mean % 1 == 0:
    print(f"Mean = {int(Mean)}")
else:
    print(f"Mean = {Mean:.2f}")

list1.sort()
print(f"sort = {list1}")

length = len(list1)-1
if length % 2 == 0:
    Median = list1[int(length/2)]
else:
    position1 = int((length/2)-0.5)
    position2 = int((length/2)+0.5)
    Median = (list1[position1]+list1[position2])/2
if Median % 1 == 0:
    print(f"Median = {int(Median)}")
else:
    print(f"Median = {Median:.2f}")

print(f"list2 =  {list2}")
print("===== End of program =====")