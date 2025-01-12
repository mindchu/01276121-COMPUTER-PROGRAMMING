print(" *** Find number of lines for specific word ***")
fname, word = input("Enter file name and word : ").split()
count = 0
wordinline_count = 0
content = open(fname)
for line in content:
    count += 1
    if word in line:
        wordinline_count += 1
print(f'Number of lines having "{word}" => {wordinline_count}')
print(f"Total lines => {count}")