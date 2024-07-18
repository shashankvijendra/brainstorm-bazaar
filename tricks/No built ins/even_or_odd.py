"""Display the number is even or odd without conditions"""


def find_even_or_odd(number):
    # Perform bitwise AND operation with 1
    bit_result = number & 1
    
    # Map the result to "Even" or "Odd" without using if conditions
    return ("Even", "Odd")[bit_result]

# Example usage
numbers = [7, 10, 15, 20]
for num in numbers:
    print(f"{num} is {find_even_or_odd(num)}")
