print(" *** Find Total lines ***")
fname = input("Enter file name : ")
content = open(fname)
print(f"property => {content}")
count = 0
for line in content:
    count += 1
print(f"Total lines : {count:,}")
print("===== End of progam =====")