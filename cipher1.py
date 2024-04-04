
alpha = ("abcdefghijklmnopqrstuvwxyz")

print("Welcome to the Caeser Cypher!")
print()

begin = input("Would you like to encode (e) or decode (d) ? ").lower()
textgiven=input("What is your text? ").lower()
shift= int(input("What is the key (1-26)?"))

def encrypt(textgiven, shift):
    encodedtext = ' '
    for letter in textgiven:
        index = alpha.find(letter)
        newalpha = index + shift
        if newalpha >= 26 :
            newalpha -=26
        encodedtext += alpha[newalpha]
    return encodedtext

def decrypt(textgiven, shift):
    decodedtext = ' '
    for letter in textgiven:
        index = alpha.find(letter)
        newalpha = index - shift
        if newalpha <0 :
            newalpha +=26
        decodedtext += alpha[newalpha]
    return decodedtext

if begin == "e":
    encodedtext = encrypt(textgiven, shift)
    print (f"Your encoded text is:", encodedtext)

if begin == "d":
    decodedtext = decrypt(textgiven, shift)
    print(f"Your decoded text is:", decodedtext)





    
