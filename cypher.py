alpha = "abcdefghijklmnopqrstuvwxyz"

def encrypt(textgiven, shift):
    encodedtext = ''
    for letter in textgiven:
        if letter in alpha:
            index = alpha.find(letter)
            newalpha = index + shift
            if newalpha >= 26:
                newalpha -= 26
            encodedtext += alpha[newalpha]
        else:
            encodedtext += letter
    return encodedtext

def decrypt(textgiven, shift):
    decodedtext = ''
    for letter in textgiven:
        if letter in alpha:
            index = alpha.find(letter)
            newalpha = index - shift
            if newalpha < 0:
                newalpha += 26
            decodedtext += alpha[newalpha]
        else:
            decodedtext += letter
    return decodedtext

def caesar_cipher():
    print("Welcome to the Caesar Cipher!")
    print()

    while True:
        begin = input("Would you like to encode (e), decode (d), or quit (q)? ").lower()
        if begin == "q":
            print("Goodbye!")
            break

        textgiven = input("What is your text? ").lower()
        shift = int(input("What is the key (1-26)?"))

        if begin == "e":
            encodedtext = encrypt(textgiven, shift)
            print(f"Your encoded text is: {encodedtext}")
        elif begin == "d":
            decodedtext = decrypt(textgiven, shift)
            print(f"Your decoded text is: {decodedtext}")
        else:
            print("Invalid option. Please enter 'e' to encode, 'd' to decode, or 'q' to quit.")
        print()  # Print a blank line for better readability

caesar_cipher()
