array = []
num = int(input("Nhập số lượng số: "))
for i in range(0, num):
    nhapso = int(input(f"Nhập số thứ {i+1}: "))
    array.append(nhapso)

tong = 0  
for i in range(len(array)):
    if 10 <= array[i] <= 50:
        tong += array[i]
if tong == 0:
    print("Không có số nào trong khoảng từ 10 -> 50")
else:
    print(f"Tổng các số trong khoảng từ 10 -> 50 là: {tong}")
    