print(" *** Pyramid-V ***")
height = int(input("Enter height : "))
row = 0
while row < height:
    col = 0
    while col < 2*height:
        if row+col == height-1:
            print("/",end="")
        elif col == (row+height):
            print("\\",end="")
        elif (row+col) >= (height-1) and col < (row+height):
            if row == height-1:
                print("_",end="")
            else:
                print(".",end="")
        else:
            print(" ",end="")
        col += 1
    print()
    row += 1
print("===== End of program =====")

