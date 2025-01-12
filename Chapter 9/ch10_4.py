print(" *** File Error Handling ***")
fname, word = input("Enter file name and word : ").split()
try:
    content = open(fname)
except:
    print(f"Error can not open file => {fname}")
    print("===== End of program =====")
    quit()

count = 0
wordinline_count = 0
sum = 0
for line in content:
    count += 1
    if word in line:
        wordinline_count += 1
        sum += count
print(f'Number of lines having "{word}" => {wordinline_count}')
print(f"Sum of line number => {sum:,}")
print(f"Total lines => {count:,}")
print("===== End of program =====")