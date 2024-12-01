"""Multiply the values without using the  * """


def multiply(a_value, b_value):
    """
    Multiply two values without using the  *  operator.
    """
    result = 0
    abs_a = abs(a_value)
    abs_b = abs(b_value)

    for _ in range(abs_b):
        result += abs_a

    if (a_value > 0 and b_value > 0) or (a_value < 0 and b_value < 0):
        return result
    else:
        return -result

# Example usage
print(multiply(5, 6))  # Should print 30
print(multiply(-3, 7))  # Should print -21
print(multiply(-4, -8))  # Should print 32

