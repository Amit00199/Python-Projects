def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():

        if not char.isalpha():
            final_message += char
        else:        
            key_char = key[key_index % len(key)]
            key_index += 1

            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            final_message += alphabet[new_index]
    
    return final_message


def encrypt(message, key):
    return vigenere(message, key)
    

def decrypt(message, key):
    return vigenere(message, key, -1)


ans = int(input('Do you want to \n1. Encrypt a message\n2. Decrypt a message\nEnter 1 or 2: '))

if ans == 1:
    message = input('Enter the message to be encrypted: ')
    key = input('Enter the key: ')
    print(f'Encrypted message: {encrypt(message, key)}')
else:
    message = input('Enter the message to be decrypted: ')
    key = input('Enter the key: ')
    print(f'Decrypted message: {decrypt(message, key)}')