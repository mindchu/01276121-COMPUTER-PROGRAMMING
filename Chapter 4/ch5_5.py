print(" *** Pyramid-XV ***")
height = int(input("Enter height : "))
alphabet = 65
line = height-1
for row in range(height): 
    print("-"*line,end="")
    for char in range(2*row+1):
        if row % 2 == 0: #row 0,2,4,...
            if char <= row:
                if alphabet > 90:
                    alphabet -= 26
                if char == 0:
                    reverse_alphabet = alphabet + row
                if reverse_alphabet < 65:
                    reverse_alphabet += 26
                elif reverse_alphabet > 90:
                    reverse_alphabet -= 26
                print(chr(reverse_alphabet),end="")
                reverse_alphabet -= 1
                alphabet += 1
            else:
                print(".",end="")
        else: #row 1,3,5,...
            if char >= row:
                if alphabet > 90:
                    alphabet -= 26
                print(chr(alphabet),end="")
                alphabet += 1
            else:
                print(".",end="")
    print("-"*line)
    line -= 1

print("===== End of program =====")