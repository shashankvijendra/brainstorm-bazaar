"""Display numbers without using the for loop"""

def display_numbers(start, end):
    """Display numbers from start to end without using a for loop."""
    if start > end:
        return
    print(start)
    display_numbers(start + 1, end)

display_numbers(1, 10)

