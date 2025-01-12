print(" *** Remove ODD characters ***")
string = input("Enter a string : ")
count = 1
print("Even characters = ",end="")
for i in string:
    if count % 2 == 0:
        print(i,end="")
    count += 1
print("\n===== End of program =====")