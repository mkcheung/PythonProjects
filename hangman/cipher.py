# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.

# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.

# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.



alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


direction = print("Type 'encode' to encrypt. Type 'decode' to decript.")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text, shift_amount):
    cipherTerm = ''
    for char in text:
        indexOfChar = alphabet.index(char)
        indexOfNewChar = indexOfChar + shift
        indexOfNewChar %= len(alphabet)
        cipherTerm += alphabet[indexOfNewChar]
    print(f"{cipherTerm}\n")

encrypt(original_text=text, shift_amount=shift)

