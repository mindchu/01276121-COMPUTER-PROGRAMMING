print("*** Minimum Occurrence ***")
num = input("Enter some numbers: ").split()
num = [int(i) for i in num]
frequency = None
for i in num:
    if frequency == None:
        frequency = i
        count = num.count(i)
    elif num.count(i) < count:
        frequency = i
        count = num.count(i)
print(frequency)