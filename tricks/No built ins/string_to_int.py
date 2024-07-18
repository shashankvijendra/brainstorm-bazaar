"""Convert the data from string to int without using the int"""


def convert_Str_to_int(x):
    res = 0
    for i in x:
        res = res*10 + (ord(i)- ord("0"))
    
    return res
a = "134"
convert_Str_to_int(a)