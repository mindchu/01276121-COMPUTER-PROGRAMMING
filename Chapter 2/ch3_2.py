print(" *** Min Max Avg ***")
num_1,num_2,num_3 = input("Enter 3 numbers : ").split()
num_1 = float(num_1)
num_2 = float(num_2)
num_3 = float(num_3)

if num_1 <= num_2 and num_1 <= num_3:
    min = num_1
elif num_2 <= num_1 and num_2 <= num_3:
    min = num_2
else:
    min = num_3

if num_1 >= num_2 and num_1 >= num_3:
    max = num_1
elif num_2 >= num_1 and num_2 >= num_3:
    max = num_2
else:
    max = num_3

if min < num_3 and num_3 < max:
    mid = num_3
elif min < num_2 and num_2 < max:
    mid = num_2
else:
    mid = num_1

print(f"min, mid, max ==> {min:.1f}, {mid:.1f}, {max:.1f}")

Average = (min+mid+max)/3

print(f"Average ==> {Average:.2f}")