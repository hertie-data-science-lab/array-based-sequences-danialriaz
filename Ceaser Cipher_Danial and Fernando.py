
# We introduce a string containing all English alphabets along with its length
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num_letters = len(letters)

# We introduce a function that takes in any text, the mode of transformation (encryption or decryption) and a key identifying by how many letters we need to move forwards or backwards (3 for the Ceaser Cipher)
def encrypt_decrypt(text, mode, key):
    result = ''
# For decryptin the key is converted to a negative number
    if mode == 'd':
        key = -key
# Anything inputed is transformed into uppercase
    for letter in text:
        letter = letter.upper()
# Blank spaces are left as it is
        if not letter == '':
            index = letters.find(letter)
# If the inputted character is not in our Alphabets, like special characters, we let it be as it is in the output
            if index == -1:
                result += letter
# Otherwise we transform the text based upon the key and mode selected
            else:
                new_index = index + key
# If after accounting for the key we exceed the number of letters (26) or become negative then we adjust for this to form the new index
                if new_index >= num_letters:
                    new_index -= num_letters
                elif new_index < 0:
                    new_index += num_letters
                result += letters[new_index]
    return result

print()
print('***CEASER CYPHER***')
print()

print('Do you want encrypt or decrypt?')
user_input = input('e/d: ').lower()
print()

if user_input == 'e':
    print("ENCRYPTION MODE SELECTED")
    print()
    key = int(input('Enter the key 1 through 26: '))
    text = input('Message: ')
    ciphertext = encrypt_decrypt(text, user_input, key)
    print(f'Secret: {ciphertext}')

elif user_input == 'd':
    print("DECRYPTION MODE SELECTED")
    print()
    key = int(input('Enter the key 1 through 26: '))
    text = input('Secret: ')
    plaintext = encrypt_decrypt(text, user_input, key)
    print(f'Message: {plaintext}')