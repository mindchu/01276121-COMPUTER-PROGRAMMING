print(" *** Adding number ***")
word = input("Enter your words : ").split()
count = 1
for i in word:
    if count % 2 == 0:
        print(f"{i[::-1]}{count}",end=" ")
    else:
        print(f"{i}{count}",end=" ")
    count += 1
print("\n==== End of program =====")
