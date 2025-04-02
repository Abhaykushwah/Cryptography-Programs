#RSA cryptosystem 
import random
import math

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

def generate_keypair(bits=64):  # Using 64 bits for demonstration
    # Generate two large prime numbers
    p = generate_prime(bits)
    q = generate_prime(bits)
    
    # Calculate n and phi
    n = p * q
    phi = (p - 1) * (q - 1)
    
    # Choose public key e (commonly 65537) // for faster and secure computation
    e = 65537
    while math.gcd(e, phi) != 1:
        e = random.randrange(2, phi)
    
    # Calculate private key d
    d = mod_inverse(e, phi)
    
    return ((e, n), (d, n))

def encrypt(message, public_key):
    e, n = public_key
    
    # Convert message to integer
    m = int.from_bytes(message.encode(), 'big')
    
    # Split message into chunks if it's too large
    chunk_size = (n.bit_length() - 1) // 8       # Size in bytes
    message_bytes = message.encode()
    chunks = [message_bytes[i:i+chunk_size] for i in range(0, len(message_bytes), chunk_size)]
    
    # Encrypt each chunk
    encrypted_chunks = []
    for chunk in chunks:
        m = int.from_bytes(chunk, 'big')
        # RSA encryption: c = m^e mod n
        c = pow(m, e, n)
        encrypted_chunks.append(c)
    
    return encrypted_chunks

def decrypt(cipher_chunks, private_key, n):
    d = private_key
    decrypted_message = ""
    
    for c in cipher_chunks:
        # RSA decryption: m = c^d mod n
        m = pow(c, d, n)
        # Convert to bytes and then to string
        try:
            chunk_bytes = m.to_bytes((m.bit_length() + 7) // 8, byteorder='big')
            decrypted_message += chunk_bytes.decode()
        except:
            decrypted_message += str(m)
    
    return decrypted_message

def main():
    print("RSA Cryptosystem Implementation")
    print("-----------------------------------")
    
    # Generate key pair
    print("\nGenerating keys...")
    try:
        public_key, private_key = generate_keypair()
        e, n = public_key
        d, _ = private_key
        
        print(f"\nPublic Key (e, n):")
        print(f"e: {e}")
        print(f"n: {n}")
        print(f"\nPrivate Key (d, n):")
        print(f"d: {d}")
        print(f"n: {n}")
        
        while True:
            print("\nOptions:")
            print("1. Encrypt a message")
            print("2. Decrypt a message")
            print("3. Exit")
            
            choice = input("\nEnter your choice (1-3): ")
            
            if choice == '1':
                message = input("\nEnter the message to encrypt: ")
                try:
                    cipher_chunks = encrypt(message, public_key)
                    print(f"\nEncrypted message chunks:")
                    for i, chunk in enumerate(cipher_chunks):
                        print(f"Chunk {i+1}: {chunk}")
                except ValueError as e:
                    print(f"\nError: {e}")
                
            elif choice == '2':
                try:
                    num_chunks = int(input("\nEnter number of chunks: "))
                    cipher_chunks = []
                    for i in range(num_chunks):
                        chunk = int(input(f"Enter chunk {i+1}: "))
                        cipher_chunks.append(chunk)
                    decrypted_message = decrypt(cipher_chunks, d, n)
                    print(f"\nDecrypted message: {decrypted_message}")
                except ValueError:
                    print("\nError: Invalid input format")
                
            elif choice == '3':
                print("\nExiting program...")
                break
            
            else:
                print("\nInvalid choice. Please try again.")
    except Exception as e:
        print(f"\nError: {e}")

if __name__ == "__main__":
    main() 