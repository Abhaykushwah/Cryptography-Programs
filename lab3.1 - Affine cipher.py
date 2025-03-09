# [Date : 29/01/2025]

# Affine cipher
# write a code to implememgt Affine cipher in such a way that first it asks for 4 options 1.Encrypt2.Decrypt3.BruteForce4.Exit. the plaintext should be only in lowercase if not print plaintext in lowercase only and  redirect to option menu. cypher text should be only in uppeercase. program should not exit until the user exits itself.

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def affine_encrypt(text, a, b):
    return ''.join([chr(((a * (ord(char) - ord('a')) + b) % 26) + ord('A')) for char in text])

def affine_decrypt(cipher, a, b):
    a_inv = mod_inverse(a, 26)
    if a_inv is None:
        return "Inverse doesn't exist"
    return ''.join([chr(((a_inv * (ord(char) - ord('A') - b)) % 26) + ord('a')) for char in cipher])

def brute_force(cipher):
    mul_key = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
    for a in range(1, 26):
        if gcd(a, 26) == 1:
            for b in mul_key:
                print(f'a={a}, b={b}: {affine_decrypt(cipher, a, b)}')

def main():
    while True:
        print("1. Encrypt\n2. Decrypt\n3. BruteForce\n4. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            text = input("Enter plaintext: ")
            if not text.islower():
                print("Enter the plaintext in small case only.")
                continue
            a = int(input("Enter a (must be coprime with 26): "))
            b = int(input("Enter b: "))
            if gcd(a, 26) != 1:
                print("a and 26 are not coprime. Please try again.")
                continue
            print("Encrypted text:", affine_encrypt(text, a, b))
        elif choice == '2':
            cipher = input("Enter ciphertext: ")
            if not cipher.isupper():
                print("Enter the ciphertext in capital letters only.")
                continue
            a = int(input("Enter a (must be coprime with 26): "))
            b = int(input("Enter b: "))
            if gcd(a, 26) != 1:
                print("a and 26 are not coprime. Please try again.")
                continue
            print("Decrypted text:", affine_decrypt(cipher, a, b))
        elif choice == '3':
            cipher = input("Enter ciphertext: ")
            if not cipher.isupper():
                print("Enter the ciphertext in capital letters only.")
                continue
            brute_force(cipher)
        elif choice == '4':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
