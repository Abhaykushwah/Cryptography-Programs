# implement hill cipher for a given key matrix. find the inverse of given key matrix and encrypt and decrypt the same.
import numpy as np

## this module from INTERNET
def mod_inverse(matrix, modulus):
    det = int(np.round(np.linalg.det(matrix)))
    det_inv = pow(det, -1, modulus)
    matrix_modulus_inv = (det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % modulus)
    return matrix_modulus_inv


def hill_encrypt(plaintext, key_matrix):
    plaintext = plaintext.lower()
    n = key_matrix.shape[0]
    while len(plaintext) % n != 0:
        plaintext += 'x' ## adding x as bogus character
    ## checking and converting
    plaintext_matrix = np.array([ord(char) - ord('a') for char in plaintext]).reshape(-1, n)
    cipher_matrix = (np.dot(plaintext_matrix, key_matrix) % 26).astype(int)
    cipher_text = ''.join(chr(num + ord('A')) for num in cipher_matrix.flatten())
    return cipher_text

def hill_decrypt(ciphertext, key_matrix):
    ciphertext = ciphertext.upper()
    n = key_matrix.shape[0]
    ## checking and converting
    cipher_matrix = np.array([ord(char) - ord('A') for char in ciphertext]).reshape(-1, n)
    key_matrix_inv = mod_inverse(key_matrix, 26)
    plaintext_matrix = (np.dot(cipher_matrix, key_matrix_inv) % 26).astype(int)
    plaintext = ''.join(chr(num + ord('a')) for num in plaintext_matrix.flatten())
    return plaintext

def main():
    while True:
        print("1. Encrypt\n2. Decrypt\n3. Print the inverse of key Matrix\n4. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            text = input("Enter plaintext: ")
            if not text.islower():
                print("Enter the plaintext in small case only.")
                continue
            key = input("Enter key matrix (comma-separated rows, space-separated values): ")
            key_matrix = np.array([list(map(int, row.split())) for row in key.split(',')])
            print("Encrypted text:", hill_encrypt(text, key_matrix))
        elif choice == '2':
            cipher = input("Enter ciphertext: ")
            if not cipher.isupper():
                print("Enter the ciphertext in capital letters only.")
                continue
            key = input("Enter key matrix (comma-separated rows, space-separated values): ")
            key_matrix = np.array([list(map(int, row.split())) for row in key.split(',')])
            print("Decrypted text:", hill_decrypt(cipher, key_matrix))
        elif choice == '3':
            key = input("Enter key matrix (comma-separated rows, space-separated values): ")
            key_matrix = np.array([list(map(int, row.split())) for row in key.split(',')])
            print("Inverse of key matrix:")
            print(mod_inverse(key_matrix, 26))
            continue
        elif choice == '4':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
    
    
    
    
    
# The Hill cipher, in essence, operates on these key theoretical steps:

#   Key Matrix:
#       A square matrix is used as the encryption key. This matrix must be invertible.
#       The dimensions of the matrix determine the size of the plaintext blocks that will be encrypted.
#   Plaintext Conversion:
#       The plaintext message is converted into numerical values, typically by assigning numbers to letters (e.g., A=0, B=1, ..., Z=25).
#       The numerical plaintext is then divided into blocks of a size that matches the key matrix dimensions.
#   Encryption (Matrix Multiplication):
#       Each plaintext block is treated as a vector.
#       This plaintext vector is multiplied by the key matrix.
#       The resulting vector is then taken modulo the size of the alphabet (typically modulo 26).
#       The resulting numerical vector is then converted back into ciphertext letters.
#   Decryption (Inverse Matrix):
#       To decrypt, the inverse of the key matrix is required.
#       The ciphertext blocks are converted to numerical vectors.
#       These vectors are multiplied by the inverse key matrix.
#       The result is taken modulo 26, and then converted back into plaintext letters.
#   Modular Arithmetic:
#       A critical aspect of the Hill cipher is the use of modular arithmetic. All calculations are performed modulo 26 (for the English alphabet), ensuring that the resulting values remain within the range of the alphabet.

# In short, it is a process of converting text to numbers, using matrix multiplication with a key, and then converting back to text, with the added complexity of needing to use the inverse of the key matrix for decryption.
