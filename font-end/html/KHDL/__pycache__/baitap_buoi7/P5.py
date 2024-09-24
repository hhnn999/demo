A = [1,3,5,9,11,2,6,8,10]
B = [1,3,5,9,11]

tongA = 0
tongB = 0

for i in range(0,len(A)):
    tongA = tongA + A[i]

for i in range(0,len(B)):
    tongB = tongB + B[i]
    
avg_A = tongA/len(A)
avg_B = tongB/len(B)

print("giá trị trung bình cộng của A: ",avg_A)
print("giá trị trung bình cộng của A: ",avg_B)