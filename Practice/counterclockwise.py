width, height = input("Enter width height: ").split()
width = int(width)
height = int(height)

result = [[0] * width for _ in range(height)]

row = 0
col = 0
count = 0
min_row = 0
min_col = 1
max_row = height - 1
max_col = width - 1

for i in range(1,width*height+1):
    result[row][col] = i
    if count % 2 == 0: # positive direction
        if row < max_row: # down
            row += 1
        elif col < max_col: # right
            col += 1
        else: # change to negative direction
            count += 1
            max_row -= 1
            max_col -= 1
            row -= 1
    else: # negative direction
        if row > min_row: # up
            row -= 1
        elif col > min_col: # left
            col -= 1
        else: # change to positive direction
            count += 1
            min_row += 1
            min_col += 1
            row += 1

for i in result:
    for j in i:
        print(f"{j:2}", end=" ")
    print()

print("===== End of program ======")