full_text = input("Enter : ")
text = full_text.split()
for word in text:
    dictionary = dict()
    for char in word:
        dictionary[char] = dictionary.get(char, 0) + 1
    print(f"{word} = {dictionary}")

if len(text) > 1:
    full_dict = dict()
    for char in full_text.replace(" ",""):
        full_dict[char] = full_dict.get(char, 0)+1
    print(f"{full_text} = {full_dict}")
    print(f"Maximum Character Count: {max(full_dict, key=full_dict.get)} {full_dict[max(full_dict, key=full_dict.get)]}")
else:
    print(f"Maximum Character Count: {max(dictionary, key=dictionary.get)} {dictionary[max(dictionary, key=dictionary.get)]}")
print("===== End of program =====")