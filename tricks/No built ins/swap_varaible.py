"""swap variables wihtout using the third variables"""


def swap_val(a,b):
    a = a+b
    b = a-b 
    a = a-b
    return a,b

a = 10
b = 20
print(swap_val(a,b))
