# ElGamal cryptosystem can be defined as the cryptography algorithm that uses the public and private key concepts to secure communication between two systems. It can be considered the asymmetric algorithm where the encryption and decryption happen by using public and private keys. In order to encrypt the message, the public key is used by the client, while the message could be decrypted using the private key on the server end. This is considered an efficient algorithm to perform encryption and decryption as the keys are extremely tough to predict. The sole purpose of introducing the message transaction’s signature is to protect it against MITM, which this algorithm could very effectively achieve. Write a program to implement Elgamal Cryptosystem to generate the pair of keys and then show the encryption & decryption of a given message.

import random

# Function to check if a number is prime
def is_prime(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

# Function to generate a large prime number
def generate_prime(bits=256):
    while True:
        n = random.getrandbits(bits)
        if n % 2 != 0 and is_prime(n):
            return n

# Function to generate ElGamal key pair
def generate_keypair(bits=256):
    p = generate_prime(bits)  # Large prime number
    g = random.randint(2, p - 1)  # Generator
    x = random.randint(1, p - 2)  # Private key
    h = pow(g, x, p)  # Public key component
    return (p, g, h), x  # (public_key, private_key)

# Function to encrypt a message
def elgamal_encrypt(public_key, message):
    p, g, h = public_key
    y = random.randint(1, p - 2)  # Random ephemeral key
    c1 = pow(g, y, p)
    s = pow(h, y, p)
    c2 = (message * s) % p
    return c1, c2

# Function to decrypt a message
def elgamal_decrypt(private_key, public_key, ciphertext):
    p, g, h = public_key
    c1, c2 = ciphertext
    s = pow(c1, private_key, p)
    s_inv = pow(s, -1, p)  # Modular inverse of s
    message = (c2 * s_inv) % p
    return message

def main():
    print("ElGamal Cryptosystem")
    print("=====================")
    
    # Generate key pair
    public_key, private_key = generate_keypair()
    
    while True:
        print("\nOptions:")
        print("1. Display Keys")
        print("2. Encrypt a Message")
        print("3. Decrypt a Message")
        print("4. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            print(f"\nPublic Key (p, g, h): {public_key}")
            print(f"Private Key (x): {private_key}")
        
        elif choice == '2':
            message = input("\nEnter a message (as a string): ")
            message_as_int = int.from_bytes(message.encode('utf-8'), 'big')  # Convert string to integer
            ciphertext = elgamal_encrypt(public_key, message_as_int)
            print(f"\nEncrypted Ciphertext: {ciphertext}")
        
        elif choice == '3':
            c1 = int(input("\nEnter c1 (part of ciphertext): "))
            c2 = int(input("Enter c2 (part of ciphertext): "))
            ciphertext = (c1, c2)
            decrypted_message_as_int = elgamal_decrypt(private_key, public_key, ciphertext)
            decrypted_message = decrypted_message_as_int.to_bytes((decrypted_message_as_int.bit_length() + 7) // 8, 'big').decode('utf-8')  # Convert integer back to string
            print(f"\nDecrypted Message: {decrypted_message}")
        
        elif choice == '4':
            print("Exiting...")
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()