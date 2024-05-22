def decode_string(s: str) -> str:
    stack = []
    current_sequence = ""
    num = 0

    for char in s:
        if char.isdigit():
            num = num * 10 + int(char)
        elif char == "[":
            stack.append((current_sequence, num))
            current_sequence, num = "", 0
        elif char == "]":
            prev_sequence, repeat = stack.pop()
            current_sequence = prev_sequence + current_sequence * repeat
        else:
            current_sequence += char

    return current_sequence

# Example usage
encoded_string1 = "3[a]2[bc]"
decoded_string1 = decode_string(encoded_string1)
print(f"Decoded string 1: {decoded_string1}")  # Output: "aaabcbc"

encoded_string2 = "3[a2[c]]"
decoded_string2 = decode_string(encoded_string2)
print(f"Decoded string 2: {decoded_string2}")  # Output: "accaccacc"
    