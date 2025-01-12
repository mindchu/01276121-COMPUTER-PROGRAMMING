inp = input("Enter width height : ")
print(inp, type(inp))
width, height = inp.split()
print(f"width={width} type={type(width)}")
print(f"height={height} type={type(height)}")
width = int(width)
height = int(height)
area = width * height
print(f"area={area}")