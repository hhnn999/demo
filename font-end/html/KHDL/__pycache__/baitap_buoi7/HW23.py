so_sinh_vien = int(input("nhập số sinh viên: "))
mon_hoc = ['Toán', 'Lý', 'Hoá', 'Anh', 'Văn']
diem = []

for i in range(0, so_sinh_vien):
    for j in range(0, 5):
        nhapdiem = int(input(f"Nhập điểm {mon_hoc[j]} của sinh viên thứ {i+1}: "))
        diem.append(nhapdiem)
        
print("========================================")        
for i in range(0, so_sinh_vien):
    tong_diem = 0
    
    for k in range(0, 5):
        tong_diem = tong_diem + diem[i * 5 + k]
    
    diem_tb_sv = tong_diem / 5
    
    print(f"Điểm trung bình của sinh viên thứ {i+1}: {diem_tb_sv}")