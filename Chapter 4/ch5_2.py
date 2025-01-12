print(" *** Maximum value ***")
value = input("Enter some numbers : ").split()
max_value = None
for i in value:
    try:
        i = int(i)
        if i == -1:
            break
        elif max_value == None:
            max_value = i
        elif i > max_value:
            max_value = i
    except:
        if i == "stop":
            break
print(f"Max value = {max_value}")
print("===== End of program =====")