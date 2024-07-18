"""Display numbers without using the for loop"""

def nums(x):
    print(x)
    if x>=100:
        return 
    return nums(x+1)

nums(1)

