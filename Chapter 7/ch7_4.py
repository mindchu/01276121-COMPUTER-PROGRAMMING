print(" *** String Diamond ***")
string = input("Enter string : ")
even = False
if len(string) % 2 == 0:
    even = True
height = int((len(string)+1)/2)
space = " "
total_space = height-1
if even:
    start = height-1
    finish = height+1
    for row in range(height*2-1):
        if row == height - 1:
            print(f"{space*total_space}{string[start:finish]}")
            start += 1
            finish -= 1
            total_space += 1
        elif row < height:
            print(f"{space*total_space}{string[start:finish]}")
            start -= 1
            finish += 1
            total_space -= 1
        else:
            print(f"{space*total_space}{string[start:finish]}")
            start += 1
            finish -= 1
            total_space += 1
else:
    start = height-2
    finish = height+1
    for row in range(height*2-1):
        if row < height:
            if row == 0:
                print(f"{space*total_space}{string[height-1]}")
                total_space -= 1
            elif row == height-1:
                print(f"{space*total_space}{string[start:finish]}")
                start += 1
                finish -= 1
                total_space += 1
            else:
                print(f"{space*total_space}{string[start:finish]}")
                start -= 1
                finish += 1
                total_space -= 1
        else:
            if row == height*2-2:
                print(f"{space*total_space}{string[height-1]}")
            else:
                print(f"{space*total_space}{string[start:finish]}")
                start += 1
                finish -= 1
                total_space += 1
print("===== End of program =====")