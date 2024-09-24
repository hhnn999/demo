A = [1,3,5,9,11,2,6,8,10]
B = [1,3,5,9,11]

minA = A[0]
for i in A:
    if i < minA:
        minA = i

minB = B[0]
for j in B:
    if j < minB:
        minB = j
        
print("Số nhỏ nhất trong danh sách A là: ", minA)
print("Số nhỏ nhất trong danh sách B là: ", minB)