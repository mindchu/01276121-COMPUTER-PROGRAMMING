print(" *** Encoding (for) ***")
word,num = input("Enter a word and a number: ").split()
num =int(num)

ok = False
if num > 0 and num < 26:
    ok = True

if ok:
    for i in word:
        if ord(i) >= 97: #char >= "a"
            char = ord(i) - num
            if char < 97:
                char -= 6
            else:
                char -= 32
        else:
            char = ord(i) - num
            if char < 65:
                char += 26
        print(chr(char),end="")
    print()
else:
    print("Number must be between 1-26")

print("===== End of program =====")