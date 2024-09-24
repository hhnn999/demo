A = [1,3,5,9,11,2,6,8,10]
B = [1,3,5,9,11]

maxA = A[0]
for i in A:
    if i > maxA:
        maxA = i

maxB = B[0]
for j in B:
    if j > maxB:
        maxB = j
        
print("Số lớn nhất trong danh sách A là: ", maxA)
print("Số lớn nhất trong danh sách B là: ", maxB)