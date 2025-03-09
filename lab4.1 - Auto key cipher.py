# Auto key cipher  [Date : 12/02/25]# Auto key cipher  [Date : 12/02/25]

def auto_key_encrypt(text, key):
    key = key+text
    key = key[:len(text)]
    cipher_text = []
    for i in range(len(text)):
        x = ((ord(text[i]) - ord('a')) + (ord(key[i]) - ord('a')) ) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return "".join(cipher_text)

def auto_key_decrypt(cipher_text, key):
    orig_text = []
    key = list(key)
    for i in range(len(cipher_text)):
        x = ((ord(cipher_text[i]) - ord('A')) - (ord(key[i]) - ord('a')) ) % 26
        x += ord('a')
        orig_text.append(chr(x))
        key.append(chr(x))
    return "".join(orig_text)

def main():
    while True:
        print("1. Encrypt\n2. Decrypt\n3. BruteForce\n4. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            text = input("Enter plaintext in LOWER CASE only : ")
            if not text.islower():
                print("Enter the plaintext in small case only.")
                continue
            key = input("Enter key: ")
            print("Encrypted text:", auto_key_encrypt(text, key))
        elif choice == '2':
            cipher = input("Enter ciphertext in UPPER CASE only: ")
            if not cipher.isupper():
                print("Enter the ciphertext in capital letters only.")
                continue
            key = input("Enter key: ")
            print("Decrypted text:", auto_key_decrypt(cipher, key))
        elif choice == '3':
            print("Brute force is not applicable for Auto Key Cipher.")
            continue
        elif choice == '4':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()