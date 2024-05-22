def myAtoi(s: str) -> int:
    # Step 1: Ignore leading whitespace
    s = s.lstrip()

    # Step 2: Check for sign
    sign = 1
    if s and (s[0] == '-' or s[0] == '+'):
        sign = -1 if s[0] == '-' else 1
        s = s[1:]

    # Step 3: Read digits until non-digit character
    num = 0
    for char in s:
        if char.isdigit():
            num = num * 10 + int(char)
        else:
            break

    # Step 4: Apply sign
    num *= sign
    
    return num

# Example usage
print(myAtoi("42"))  # Output: 42
print(myAtoi("   -42"))  # Output: -42
print(myAtoi("4193 with words"))  # Output: 4193
