input_value0 = "3[a]2[bc]"
output = "aaabcbc"

input_value1 = "3[a]2[bc3[d]]"
output = "aaabcdddbcddd"

input_2 = "3[a2[b]]"
output = "abbabbabb"

        
def decode_string(input_str):
    """
    This function takes a string containing encoded information and decodes it to return the original string.
    It iterates through the input string and decodes it based on the encoded pattern.
    The function returns the decoded string.
    """
    stack = []
    num = 0
    current_str = ''
    
    for char in input_str:
        if char.isdigit():
            num = num * 10 + int(char)
        elif char == '[':
            stack.append((current_str, num))
            current_str = ''
            num = 0
        elif char == ']':
            prev_str, prev_num = stack.pop()
            current_str = prev_str + current_str * prev_num
        else:
            current_str += char
            
    return current_str

print(decode_string(input_2))