def sortalpha(t):
    return t[::-1]

print(" *** Histogram ***")
fname, word = input("Enter file name and word : ").split()
try:
    content = open(fname)
except:
    print(f"Error can not open file => {fname}")
    print("===== End of program =====")
    quit()

count = 0
word_count = 0
sum = 0
counts = dict()

for line in content:
    count += 1
    if word in line:
        word_count += line.count(word)
        sum += count
        for char in line:
            if char.isalpha():
                counts[char] = counts.get(char,0) + 1

print(f'Number of "{word}" => {word_count}')
print(f"Sum of line number => {sum:,}")
print(f"Total lines => {count:,}")

sort_counts = sorted(counts.items(), key=sortalpha , reverse = True)[:3]
most_count = 0
for char, frequency in sort_counts:
    print(f" {char}  => {'*'*frequency:<{most_count}} {frequency:02}")
    if most_count == 0:
        most_count = frequency

print("===== End of program =====")
