#multiplicative cipher

# write a code to implememgt multiplicative cipher in such a way that first it asks for 4 options 1.1.Encrypt2.Decrypt3.BruteForce4.Exit. the plaintext should be only in lowercase if not print plaintext in lowercase only and  redirect to option menu. cypher text should be only in uppeercase. program should not exit until the user exits itself.


# multiplicative cipher

import sys

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return -1

while(True):
    print('''
    1.Encrypt
    2.Decrypt
    3.BruteForce
    4.Exit
    ''')

    user_input = int(input("Enter Your Choice: "))

    if(user_input == 1):
        text = input("enter the text for encryption: ")
        k = int(input("Enter the multiplicative key: "))
        def encrypt(text, k):
            res = ""
            for i in range(len(text)):
                char = text[i]
                if (char.isupper()):
                    res += "enter the text in small case only!"
                    return res
                else:
                    res += chr(((ord(char) - 97) * k % 26) + 97)
            res = res.upper()
            return res
        print(encrypt(text, k))

    if(user_input == 2):
        text = input("enter the text for decryption: ")
        k = int(input("Enter the multiplicative key: "))
        def decrypt(text, k):
            res = ""
            if(text.islower()):
                res += "enter the text in Upper case only!"
                return res
            text = text.lower()
            k_inv = mod_inverse(k, 26)
            if k_inv == -1:
                return "Multiplicative inverse not found!"
            for i in range(len(text)):
                char = text[i]
                if (char == " "):
                    res += " "
                elif (char.islower()):
                    res += chr(((ord(char) - 97) * k_inv % 26) + 97)
            res = res.lower()
            return res
        print(decrypt(text, k))

    if(user_input == 3):
        text = input("enter the text for decryption: ")
        def brute_force(text):
            if(text.islower()):
                print("enter the text in Upper case only!")
                return
            text = text.lower()
            for k in range(1, 26):
                k_inv = mod_inverse(k, 26)
                if k_inv == -1:
                    continue
                res = ""
                for i in range(len(text)):
                    char = text[i]
                    if (char == " "):
                        res += " "
                    elif (char.islower()):
                        res += chr(((ord(char) - 97) * k_inv % 26) + 97)
                print(f"Key {k}: {res.lower()}")
        brute_force(text)

    if(user_input == 4):
        sys.exit()