"""Find the len of the array without using the len"""

def find_length(iterable):
    length = 0
    for _ in iterable:
        length += 1
    return length

# Input: [1,2,3,4,5,6]
# Output: 6

def list_length(list_):
    """
    Recursively calculates the length of a list without using the len() function.

    Args:
        list_ (list): The list whose length is to be calculated.

    Returns:
        int: The length of the list.
    """
    # Base case: if the list is empty, return 0
    if not list_:
        return 0
    
    # Recursive case: return 1 plus the length of the rest of the list
    return 1 + list_length(list_[1:])



def list_length(lst):
    """
    Calculates the length of a list without using the len() function.
    
    Args:
        lst (list): The list whose length is to be calculated.
    
    Returns:
        int: The length of the list.
    """
    # Use the sum() function with a generator expression to count the number of elements in the list
    # The generator expression uses the map() function to apply a lambda function to each element in the list
    # The lambda function simply returns 1 for each element, which is then summed up to give the length of the list
    return sum(map(lambda x: 1, lst))
