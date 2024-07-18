"""Multiply the values without using the  * """


def multiply(a, b):
    result = 0
    # Determine the absolute values to handle negative numbers correctly
    abs_a = abs(a)
    abs_b = abs(b)
    
    # Use a loop to add 'a' to itself 'b' times
    for _ in range(abs_b):
        result += abs_a
    
    # Determine the sign of the result based on the signs of 'a' and 'b'
    if (a > 0 and b > 0) or (a < 0 and b < 0):
        return result
    else:
        return -result

# Example usage
print(multiply(5, 6))  # Should print 30
print(multiply(-3, 7))  # Should print -21
print(multiply(-4, -8))  # Should print 32
