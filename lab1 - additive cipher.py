# additive cipher OR cieser cipher

import  sys

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
        k = int(input("Enter the shift key: "))
        def encrypt(text,k):
            res = ""

            for i in range(len(text)):
                char = text[i]

                if (char.isupper()):
                    res += "enter the text in small case only!"
                    return res

                else:
                    res += chr((ord(char) + k - 97) % 26 + 97)

            res = res.upper()
            return res
        print( encrypt(text,k))

    if (user_input == 2):
        text = input("enter the text for decryption: ")
        k = int(input("Enter the shift key: "))

        def decrypt(text, k):
            res = ""
            if(text.islower()):
                res += "enter the text in Upper case only!"
                return res

            text = text.lower()
            for i in range(len(text)):
                char = text[i]

                if (char == " "):
                    res += " "

                elif (char.islower()):
                    res += chr((ord(char) - k - 97) % 26 + 97)

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
            for k in range(26):
                res = ""

                for i in range(len(text)):
                    char = text[i]
                    if (char == " "):
                        res += " "
                    elif (char.islower()):
                        res += chr((ord(char) - k - 97) % 26 + 97)
                print(f"Key {k}: {res.lower()}")

        brute_force(text)


    if(user_input == 4):
        sys.exit()