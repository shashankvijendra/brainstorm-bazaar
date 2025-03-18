n = 6

#output : 
# 1
# 2  4
# 3  5  7
# 6  8  10 12
# 9  11 13 15 17
# 14 16 18 20 22 24

sum = 1
prev = 0
vs = 0
print(1)
for i in range(1,n):
    res = 0
    vs += 1
    for j in range(i+1):
        if j == 0:
            res += i+sum+prev
            print(i+sum+prev, end=" ")
        else:
            print(res+2*j, end=" ")
    if vs>=2:
        sum += 1
        vs = 0
    prev = i
    print("", end="\n")
