# play fair ciper [Date : 12/02/25]

def playfair_encrypt():
    return
def playfair_decrypt():
    return


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
            print("Encrypted text:",playfair_encrypt(text, key))
        elif choice == '2':
            cipher = input("Enter ciphertext in UPPER CASE only: ")
            if not cipher.isupper():
                print("Enter the ciphertext in capital letters only.")
                continue
            key = input("Enter key: ")
            print("Decrypted text:", playfair_decrypt(cipher, key))
        elif choice == '3':
            print("Brute force is not applicable for playfair Key Cipher.")
            continue
        elif choice == '4':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()