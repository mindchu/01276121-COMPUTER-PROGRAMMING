height = int(input("Enter height : "))
row = 0
count = 0
while row < height:
    col = 0
    while col < 2*height:
        if row+col >= height-1 and col < row+height:
            print(chr(97+count),end="")
            count += 1
            if count > 25 :
                count = 0
        else:
            print(" ",end="")
        col += 1
    print()
    row += 1