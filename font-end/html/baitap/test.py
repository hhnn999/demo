hang = int(input("Nhập số hàng của ma trận: "))
cot = int(input("Nhập số cột của ma trận: "))

matrix = []

for i in range(hang):
    row = []
    for j in range(cot):
        element = int(input(f"nhập phần tử ở hàng {i+1} cột {j+1}: "))
        row.append(element)
    matrix.append(row)

#Tính số hàng của ma trận
num_rows = len(matrix) 

print(f"Số hàng của ma trận là: {num_rows}")   
    
#Tính số cột của ma trận
num_columns = len(matrix[0]) if matrix else 0

print(f"Số cột của ma trận là: {num_columns}")   

#Đếm số chẵn trong hàng của ma trận
row_to_count = int(input("Nhập hàng bạn muốn đếm số chẵn: ")) - 1

even_count = 0 
for element in matrix[row_to_count]:
    if element % 2 == 0:
        even_count += 1
        
print(f"Số số chẵn trong hàng {row_to_count+1} của ma trận là: {even_count}")