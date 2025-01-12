# Assign decrypt key to variable named cipher_key
cipher_key = {
    ('A', 'A'): 'b',
    ('A', 'D'): 't',
    ('A', 'F'): 'a',
    ('A', 'G'): 'l',
    ('A', 'X'): 'p',

    ('D', 'A'): 'd',
    ('D', 'D'): 'h',
    ('D', 'F'): 'o',
    ('D', 'G'): 'z',
    ('D', 'X'): 'k',

    ('F', 'A'): 'q',
    ('F', 'D'): 'f',
    ('F', 'F'): 'v',
    ('F', 'G'): 's',
    ('F', 'X'): 'n',

    ('G', 'A'): 'g',
    ('G', 'D'): 'i/j',
    ('G', 'F'): 'c',
    ('G', 'G'): 'u',
    ('G', 'X'): 'x',

    ('X', 'A'): 'm',
    ('X', 'D'): 'r',
    ('X', 'F'): 'e',
    ('X', 'G'): 'w',
    ('X', 'X'): 'y',
}

# Receive the input text from user and assign to variable named cipher
text = input("Input ADFGX cipher text: ")
# Check if the input text is not in uppercase letters
if text != text.upper():
    # If the input text have lowercase letters, print "FAILED TO DECRYPT" message on the screen
    print("FAILED TO DECRYPT")
# Check if the total letters of the text is not even number
elif len(text) % 2 != 0:
    # If the total letters of the text is odd number, print "FAILED TO DECRYPT" message on the screen
    print("FAILED TO DECRYPT")
# If the input text is in uppercase letters and the total letters of the text is even number, run the code below
else: 
    # Assign False to variable named character_error to check if the input text in the right format
    character_error = False
    # Create a loop to check each letter in the input text
    for character in text:
        # Check if the letter from the input text is not "A","D","F","G","X"
        if character not in ["A","D","F","G","X"]:
            # If the letter is not "A","D","F","G","X", set the variable character_error to True
            character_error = True
            # Then print "FAILED TO DECRYPT" message on the screen
            print("FAILED TO DECRYPT")
            # Terminate this loop
            break
    # Assign 0 to variable named count to check which position this letter is in the text
    count = 0
    # If the variable character_error is still False, run the code below
    if character_error == False:
        # Create a loop to check each letter in the input text
        for character in text:
            # If the value of count variable is even number, run the code below
            if count % 2 == 0:
                # Print the value of keys which is the current letter and the next letter of the loop
                print(cipher_key[character,text[count+1]],end="")
            # Add 1 to variable count
            count += 1