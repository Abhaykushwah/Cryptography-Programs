# impememt the rsa didgital signature for any kind of message showing the digital sign in such a scenario for encryption and decryption
import random
import math
import hashlib  # Add hashlib for SHA-256

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

def generate_prime(bits):
    while True:
        n = random.getrandbits(bits)
        if n % 2 != 0 and is_prime(n):
            return n

def mod_inverse(e, phi):
    def extended_gcd(a, b):
        if a == 0:
            return b, 0, 1
        gcd, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y

    gcd, x, y = extended_gcd(e, phi)
    if gcd != 1:
        raise ValueError("Modular inverse does not exist")
    return x % phi

def generate_keypair(bits=1024):  # Increased key size for security
    p = generate_prime(bits)
    q = generate_prime(bits)
    n = p * q
    phi = (p - 1) * (q - 1)
    
    e = 65537  # Commonly used value for e
    while math.gcd(e, phi) != 1:
        e = random.randrange(2, phi)
    
    d = mod_inverse(e, phi)
    return ((e, n), (d, n))   ##  (public_key, private_key)

def sign_message(message, private_key):
    d, n = private_key
    # Hash the message first
    hash_obj = hashlib.sha256(message.encode())
    message_hash = int.from_bytes(hash_obj.digest(), 'big')
    # Create signature
    signature = pow(message_hash, d, n)    ### [M pow(d) * (mod n)]
    return signature

def verify_signature(message, signature, public_key):
    e, n = public_key
    # Hash the message first
    hash_obj = hashlib.sha256(message.encode())
    message_hash = int.from_bytes(hash_obj.digest(), 'big')
    # Verify signature
    decrypted_signature = pow(signature, e, n)    ### [M pow(e) * (mod n)]
    return message_hash == decrypted_signature

def main():
    print("RSA Digital Signature Implementation")
    print("-----------------------------------")
    
    # Generate key pair
    public_key, private_key = generate_keypair()
    print(f"\nGenerated Public Key (e,n): {public_key}")
    print(f"Generated Private Key (d,n): {private_key}")
    
    while True:
        print("\nOptions:")
        print("1. Sign a message")
        print("2. Verify a signature")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == '1':
            message = input("\nEnter the message to sign: ")
            signature = sign_message(message, private_key)
            print(f"\nMessage: {message}")
            print(f"Digital Signature: {signature}")
            
        elif choice == '2':
            message = input("\nEnter the message to verify: ")
            signature = int(input("Enter the signature: "))
            is_valid = verify_signature(message, signature, public_key)
            if is_valid:
                print("\nSignature is valid! Message is authentic.")
            else:
                print("\nSignature is invalid! Message may have been tampered with.")
                
        elif choice == '3':
            print("\nExiting program...")
            break
            
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()

