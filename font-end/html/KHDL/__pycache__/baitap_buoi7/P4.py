A = [1,3,5,9,11,2,6,8,10]
B = [1,3,5,9,11]

tongA = 0
tongB = 0

for i in range(0,len(A)):
    tongA = tongA + A[i]

for i in range(0,len(B)):
    tongB = tongB + B[i]
    
C = tongA/tongB
    
print("Tổng của A:", tongA)
print("Tổng của B:", tongB)
print("C = A/B = ",C)
