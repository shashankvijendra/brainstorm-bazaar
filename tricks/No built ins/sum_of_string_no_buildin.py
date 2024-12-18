def string_to_integer(s):
    result = 0
    for char in s:
        digit = ord(char) - ord('0')
        if not 0 <= digit <= 9:
            raise ValueError(f"Invalid character '{char}' in string")
        result = result * 10 + digit
    return result

def sum_strings_as_integers(string1, string2):
    """Return the sum of two strings interpreted as integers."""
    int1 = string_to_integer(string1)
    int2 = string_to_integer(string2)
    return int1 + int2

# Example usage
try:
    result = sum_strings_as_integers("123", "456")
    print(f"The sum is: {result}")
except ValueError as e:
    print(e)
