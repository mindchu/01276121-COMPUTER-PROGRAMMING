print(" *** Creating Dictionary ***")
text = input("Enter text : ").split()
count = 0
dictionary = dict()
for i in text:
    if i in dictionary:
        dictionary[i] = dictionary[i]+int(text[count+1])
    else:
        if count % 2 == 0:
            dictionary[i] = int(text[count+1])
    count += 1
print(dictionary)
print("===== End of program =====")