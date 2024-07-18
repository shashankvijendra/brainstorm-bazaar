"""Without using the compare operator find the max values"""

def find_maximum(a, b):
    # Subtract 'b' from 'a' and check the sign of the result
    difference = a - b
    # If the difference is greater than zero, 'a' is larger
    # If the difference is less than zero, 'b' is larger
    # If the difference is exactly zero, 'a' and 'b' are equal
    if difference >> 31 & 1:  # Check the sign bit in a 32-bit integer representation
        return b
    else:
        return a

# Example usage
print(find_maximum(10, 20))  # Should print 20
print(find_maximum(30, 15))  # Should print 30
print(find_maximum(5, 5))    # Should print 5
