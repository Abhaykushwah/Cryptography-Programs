# [Date : 29/01/2025]

# Vigenere Cipher
# write a code to implement Vigenere Cipher in such a way that first it asks for 4 options 1.Encrypt2.Decrypt3.BruteForce4.Exit. the plaintext should be only in lowercase if not print plaintext in lowercase only and  redirect to option menu. cypher text should be only in uppercase. program should not exit until the user exits itself.

def generate_key(text, key):
    key = list(key)
    if len(text) == len(key):
        return key
    else:
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def encrypt(text, key):
    cipher_text = []
    key = generate_key(text, key)
    for i in range(len(text)):
        char = text[i]
        x = (ord(text[i]) + ord(key[i]) - 2 * ord('a')) % 26
        x = chr((ord(char) + ord(key[i]) - 2 * ord('a')) % 26 + ord('a'))
        x += ord('A')
        cipher_text.append(chr(x))
    return "".join(cipher_text)

def decrypt(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) - ord(key[i]) + 26) % 26
        x += ord('a')
        orig_text.append(chr(x))
    return "".join(orig_text)

while(True):
    print('''
    1.Encrypt
    2.Decrypt
    3.BruteForce
    4.Exit
    ''')

    user_input = int(input("Enter Your Choice: "))

    if(user_input == 1):
        text = input("Enter the text for encryption: ")
        key = input("Enter the key: ")
        if not text.islower():
            print("Plaintext should be in lowercase only!")
            continue
        key = generate_key(text, key)
        cipher_text = encrypt(text, key)
        print(f"Encrypted text: {cipher_text}")

    elif(user_input == 2):
        cipher_text = input("Enter the text for decryption: ")
        key = input("Enter the key: ")
        if not cipher_text.isupper():
            print("Cipher text should be in uppercase only!")
            continue
        key = generate_key(cipher_text.lower(), key)
        orig_text = decrypt(cipher_text, key)
        print(f"Decrypted text: {orig_text}")

    elif(user_input == 3):
        print("Brute force is not applicable for Vigenere Cipher.")
        continue

    elif(user_input == 4):
        break
    else:
        print("Please enter a valid option")