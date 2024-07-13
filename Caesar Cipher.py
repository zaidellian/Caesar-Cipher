def Caesar_Cipher_Encryption(plaintext, shift):
    encrypted = ""
    for char in plaintext:
        if char.isalpha():
            shifts = shift % 26
            if char.isupper():
                shifted_char = chr((ord(char) + shifts - 65) % 26 + 65)
            else:
                shifted_char = chr((ord(char) + shifts - 97) % 26 + 97)
            encrypted += shifted_char
        else:
            encrypted += char
    return encrypted

def Caesar_Cipher_Decryption(ciphertext, shift):
     decrypted = ""
     for char in ciphertext:
        if char.isalpha():
            shifts = shift % 26
            if char.isupper():
                decrypted_char = chr((ord(char) - shifts - 65) % 26 + 65)
            else:
                decrypted_char = chr((ord(char) - shifts - 97) % 26 + 97)
            decrypted += decrypted_char
        else:
            decrypted += char
     return decrypted


plaintext = input('Enter the text you want to encrypt: ')
shift = int(input('Enter the key for encryption: '))
encryption = Caesar_Cipher_Encryption(plaintext, shift)
print(f'The encryption text is : {encryption}')
ciphertext = input('Enter the text you want to decrypt: ')
shifts = int(input('Enter the key for decription: '))
decryption = Caesar_Cipher_Decryption(ciphertext, shift)
print(f'The decrypted text is: {decryption}')
