"""Find the missing int values in a list"""


def find_missing_sum(numbers, range_number):
    expected_sum = sum(range(range_number))  # Calculate the sum of numbers from 0 to 100
    actual_sum = sum(numbers)       # Calculate the sum of the given numbers
    missing_number = expected_sum - actual_sum
    return missing_number

find_missing_sum(range(100), 100)

