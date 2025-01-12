print(" *** Data type integer float string ***")
inp = input("Enter a word : ")
try:
    if float(inp) % 1 == 0:
        print(f"{int(inp)} * 2 = {(int(inp) * 2)}")
    else:
        print(f"{float(inp):.3f} / 3 = {(float(inp) / 3):.3f}")
except:
    print((str(inp)+" ")*3)