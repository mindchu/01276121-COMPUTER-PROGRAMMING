print(" *** Palindrome Checker ***")
word = input("Enter words : ").split()
for i in word:
    if len(i) == 1:
        print(f"{i} => Error!!!")
    elif i == i[::-1]:
        print(f"{i} is is palindrome")
    else:
        print(f"{i} is not palindrome")
print("===== End of progam =====")