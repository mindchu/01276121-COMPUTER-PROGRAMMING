print(" *** Creating Dictionary ***")
text = input("Enter text : ").split()
count = 0
dictionary = dict()
for i in text:
    if count % 2 == 0:
        dictionary[i] = text[count+1]
    count += 1
print(dictionary)
print("===== End of program =====")