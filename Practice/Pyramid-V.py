print(" *** Pyramid-V ***")
height = int(input("Enter height : "))
i = 0
blank = " "
dat = "_"
dot = "."
while i < height:
    if i == 0:
        print(f"{blank*(height-1)}/\\")
    elif i == height-1:
        print(f"/{dat*((2*height)-2)}\\")
    else:
        print(f"{blank*(height-i-1)}/{dot*(2*i)}\\")
    i += 1