print(" *** Center-starting Spiral Rectangle ***")
inp = input("Enter side direction: ").split()
if len(inp) == 2:
    side = inp[0]
    direction = inp[1]
    start = 1
else:
    side = inp[0]
    direction = inp[1]
    start = int(inp[2])
side = int(side)
result = [[0]*side for _ in range(side)]
if side % 2 == 0:
    row = int(side/2-1)
    col = int(side/2-1)
else:
    row = int(side/2)
    col = int(side/2)
result[row][col] = start

for i in range(start+1,start+(side*side)):
    if direction == "up":
        row -= 1
        if result[row][col+1] == 0:
            direction = "right"
        else:
            direction = "up"
    elif direction == "right":
        col += 1
        if result[row+1][col] == 0:
            direction = "down"
        else:
            direction = "right"
    elif direction == "down":
        row += 1
        if result[row][col-1] == 0:
            direction = "left"
        else:
            direction = "down"
    elif direction == "left":
        col -= 1
        if result[row-1][col] == 0:
            direction = "up"
        else:
            direction = "left"

    result[row][col] = i

length = int(len(str((side*side))))
for i in result:
    for j in i:
        print(f"{j:{length}}",end=" ")
    print()
print("===== End of program ======")