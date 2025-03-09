# WAP to implement rabin miller primality testing to check whether a given number is prime or composite.

import random

def is_prime(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Write (n - 1) as 2^r * d
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


def main():
    num = int(input("Enter a number to check for primality: "))
    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is a composite number.")


if __name__ == "__main__":
    main()
    
    
    
    
# The Rabin-Miller primality test is a probabilistic algorithm used to determine if a number is likely prime. Here's a concise overview of its theoretical steps:   

# Foundation:
#   It builds upon Fermat's Little Theorem and properties of square roots modulo a prime number.
# Preparation:
#   Given an odd number 'n' to test, express n-1 as 2^s * d, where 'd' is odd.
#   Choose a random integer 'a' (the base) between 2 and n-2.
# Testing:
#   Calculate a^d (mod n). If it's 1, 'n' is likely prime.
#   If not, calculate a^(2^r * d) (mod n) for r = 0 to s-1.
#   If any of these results is -1 (or n-1), 'n' is likely prime.
#   If none of the above conditions are met, 'n' is composite.
# Probability:
#   If 'n' passes the test for multiple random bases 'a', the probability of 'n' being prime increases significantly.
#   If a number is composite, the test will reveal that with a probability of at least 75%.
# Key Idea:
#   It leverages the fact that if 'n' is prime, certain modular arithmetic properties must hold. If they don't, 'n' is definitely composite.   


# In essence, it's a series of modular exponentiation calculations that check for specific patterns that prime numbers exhibit.