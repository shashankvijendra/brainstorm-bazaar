"""Find the len of the array without using the len"""

def find_len(x):
    count = 0
    for _i in x:
        count += 1
    return count

# Input: [1,2,3,4,5,6]
# Output: 6