print(" *** Rectangle down-left-up-left ***")
width, height = input("Enter width height : ").split()
width = int(width)
height = int(height)
result = [[0]*width for _ in range(height)]
row = 0
col = width-1
count = 0
for i in range(width*height):
    result[row][col] = i+1
    if count%2 == 0:
        if row < height-1:
            row += 1
        else:
            col -= 1
            count += 1
    else:
        if row == 0:
            col -= 1
            count += 1
        else:
            row -= 1
for i in result:
    for j in i:
        print(f"{j:3}",end="")
    print()
print("===== End of program =====")
