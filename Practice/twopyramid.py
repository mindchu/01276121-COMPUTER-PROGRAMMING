height = int(input("Enter height : "))
for row in range(height):
    for col in range(4*height):
        if row + col >= height-1 and col < row + height:
            print("*",end="")
        elif row+col >= 3*height-3 and col < row + (3*height-2):
            print("*",end="")
        else:
            print(" ",end="")
    print()