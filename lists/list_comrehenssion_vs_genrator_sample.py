# Create a list of even numbers from 0 to 10
even_numbers = [i for i in range(11) if i % 2 == 0]
print(even_numbers)  # Output: [0, 2, 4, 6, 8, 10]


# Create a generator for even numbers from 0 to 10
even_generator = (i for i in range(11) if i % 2 == 0)
for num in even_generator:
    print(num, end=" ")  # Output: 0 2 4 6 8 10
