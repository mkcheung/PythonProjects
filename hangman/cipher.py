import art

print(art.logo)

active = True

while active:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    direction = input("Type 'encode' to encrypt. Type 'decode' to decrypt.\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def encrypt(original_text, shift_amount):
        cipherTerm = ''
        for char in original_text:
            if char not in alphabet:
                cipherTerm += char
                continue
            indexOfChar = alphabet.index(char)
            indexOfNewChar = indexOfChar + shift_amount
            indexOfNewChar %= len(alphabet)
            cipherTerm += alphabet[indexOfNewChar]
        print(f"{cipherTerm}\n")

    def decrypt(original_text, shift_amount):
        decryptedTerm = ''
        shift_amount *= -1
        for char in original_text:
            if char not in alphabet:
                decryptedTerm += char
                continue
            originalCharIndex = alphabet.index(char)
            newCharIndex = originalCharIndex + shift_amount
            newCharIndex %= len(alphabet)
            decryptedTerm += alphabet[newCharIndex]
        print(f"{decryptedTerm}\n")


    def caesar(direction, text, shift):
        if(direction == 'encode'):
            encrypt(original_text=text, shift_amount=shift)
        elif(direction == 'decode'):
            decrypt(original_text=text, shift_amount=shift)
        else:
            print("Invalid Selection")

    caesar(direction=direction, text=text, shift=shift)
    stillActive = input("Do you want to try again?\nPlease enter True or False\n")
    if stillActive == 'False':
        active = False
        print('Goodbye')