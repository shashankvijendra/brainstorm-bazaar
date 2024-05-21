def is_prime(x):
    """
    Checks if a number is prime.
    """
    return True if x in [2, 3] else not any(x % n == 0 for n in range(2, int(x ** 0.5) + 1))

def manipulate_generator(generator, n):
    """
    Generates the first n non-prime numbers and converts them to prime numbers.
    """
    prime_numbers = []
    non_prime_numbers = []
    
    for _ in range(n):
        num = next(generator)
        if is_prime(num):
            prime_numbers.append(num)
        else:
            non_prime_numbers.append(num)
    
    return non_prime_numbers, prime_numbers

def positive_integers_generator():
    """
    Generates positive integers.
    """
    n = 1
    while True:
        x = yield n
        if x is not None:
            n = x
        else:
            n += 1

# Example usage:
k = int(input("Enter the value of n: "))
g = positive_integers_generator()

# Print the first n non-prime numbers
non_prime, prime = manipulate_generator(g, k)
print("First", k, "non-prime numbers:", non_prime)
print("Converted to prime numbers:", prime)
