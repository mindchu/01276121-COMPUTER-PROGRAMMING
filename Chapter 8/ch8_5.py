def generate_spiral(side):
    side = int(side)
    result = [[0]*side for row in range(side)]
    return result,side

def startpoint(side):
    if side % 2 == 0:
        row = int(side/2)+1
        col = int(side/2)+1
    else:
        row = int(side/2)
        col = int(side/2)
    return row, col

def spiral_num(spiral_rectangle, row, col, word):
    result, side = spiral_rectangle
    for num in range(word, side*side+1):
        result[row][col] = word

def spiral_char(spiral_rectangle, row, col, word):
    result, side = spiral_rectangle

    result[row][col] = word

def print_spiral(spiral_rectangle):
    result,side = spiral_rectangle
    for row in result:
        for col in row:
            print(f"{col:{len(str(side*side))}}",end=" ")
        print()

# Do NOT Modify the following code
print(" *** Center-starting Spiral Rectangle XXX ***")
inp = input("Enter side [direction] [word] : ")

args = inp.split()

# Chcek if there are more than one input
side, direction, word = None, "right", 1
if len(args) == 2:
    direction = args.pop(1)
else:
    direction = args.pop(1)
    word = args.pop(1)

# Generate and print the spiral
spiral_rectangle = generate_spiral( *args)

# Generate start point
side = spiral_rectangle[1]
row, col = startpoint(side)

# Generate the spiral
try:
    word = int(word)
    spiral_rectangle = spiral_num(spiral_rectangle, row, col, word)
except:
    spiral_rectangle = spiral_char(spiral_rectangle, row, col, word)

print_spiral(spiral_rectangle)

print("===== End of program ======")
