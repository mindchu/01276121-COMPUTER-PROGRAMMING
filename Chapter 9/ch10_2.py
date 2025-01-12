print(" *** Find Empty lines ***")
fname = input("Enter file name : ")
content = open(fname)
empty_count = 0
count = 0
for line in content:
    if line.strip() == "":
        empty_count += 1
    count += 1
print(f"Empty lines => {empty_count}")
print(f"Total lines => {count}")