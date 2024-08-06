"""Add 2 number without using addition and subtraction operators"""


def add_two_numbers(x, y):
    # Iterate until there's nothing to carry
    while y:
        # Carry now contains common set bits of x and y
        carry = x & y
        
        # Sum of bits of x and y where at least one of the bits is not set
        x = x ^ y
        
        # Carry is shifted by one so that adding it to x gives the required sum
        y = carry << 1
    
    return x

# Example usage
num1 = 5
num2 = 7
result = add_two_numbers(num1, num2)
print(f"The sum of {num1} and {num2} is {result}")

