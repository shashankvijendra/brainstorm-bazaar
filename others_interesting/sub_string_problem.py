

def count_repeating_combinations(pointer, combination):
    """
    This function takes a pointer string and a combination size and returns the total number of repeating combinations
    that can be created from the pointer string. For example, if the pointer string is "xyzxy" and the combination size
    is 3, the output will be 3, since the three possible combinations are "xyz", "xyx", and "xxy".
    
    The function works by iterating through the pointer string and checking for repeating combinations. It keeps track of
    the number of repeating combinations seen so far and adds to that number every time it sees a new repeating combination.
    It then returns the total number of repeating combinations seen.
    """
    res = 1 if (len(pointer)<combination) else 0
    
    pointer_count = len(pointer)
    vs = pointer_count
    while vs <= combination:
        start = 0
        for i, val in enumerate(pointer):
            if i==0:
                continue
            if pointer[i]==pointer[0]:
                if pointer[i:] == pointer[pointer_count-i+1]:
                    start = pointer_count-i+1
                    break
        if start:    
            vs += start
        else:
            vs += pointer_count
        
        res += 1
    return res


    
    
s1 = "xyzxy"
for i in range(11):
    target1 = i
    print(target1,count_repeating_combinations(s1, target1))  # Output: 3    