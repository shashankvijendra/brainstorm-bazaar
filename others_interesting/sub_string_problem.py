



def count_repeating_combinations(pointer, combination):
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