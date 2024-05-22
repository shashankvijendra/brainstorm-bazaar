def reverse_integer(x: int) -> int:
    # Handle the sign
    sign = 1 if x >= 0 else -1
    x = abs(x)

    # Convert to string, reverse, and convert back to integer
    reversed_str = str(x)[::-1]
    reversed_int = int(reversed_str) * sign

    return reversed_int

# Example usage
x1 = 123
x2 = -123
x3 = 120

print("Output for x =", x1, ":", reverse_integer(x1))
print("Output for x =", x2, ":", reverse_integer(x2))
print("Output for x =", x3, ":", reverse_integer(x3))
