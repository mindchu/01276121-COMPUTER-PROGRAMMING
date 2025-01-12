def addnum(row, col, num, max_col, max_row, min_col, min_row):
    cake[row][col] = num
    while col < max_col:
        cake[row][col] = num
        col += 1
    while row < max_row:
        cake[row][col] = num
        row += 1
    while col > min_col:
        cake[row][col] = num
        col -= 1
    while row > min_row:
        cake[row][col] = num
        row -= 1

size, outermost_layer = map(int, input("Enter size and outermost layer : ").split())
cake = [[0]*size for i in range(size)]
row = 0
col = 0
if size % 2 == 0:
    layers = int(size/2)
else:
    layers = int(size/2)+1
num = outermost_layer
max_col, max_row = size-1,size-1
min_col, min_row = 0,0
for layer in range(layers):
    addnum(row, col, num, max_col, max_row, min_col, min_row)
    row += 1
    col += 1
    min_col += 1
    min_row += 1
    num -= 1
    max_col -= 1
    max_row -= 1

for row in cake:
    for col in row:
        print(f"{col:{len(str(outermost_layer))+1}}",end="")
    print()