class CustomLength:
    def __init__(self, s):
        self.s = s

    def find_length(self):
        count = 0
        for char in self.s:
            count += 1
        return count

# Example usage
my_string = "Hello, world!"
custom_length_calculator = CustomLength(my_string)
length = custom_length_calculator.find_length()
print("Length of the string:", length)  # Output: 13
