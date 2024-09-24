
        
# Radmin VPN

so_sinh_vien = int(input("Nhập số lượng sinh viên: "))
so_hoc_phan = int(input("Nhập số lượng môn học: "))

sinh_vien = []
for i in range(0, so_sinh_vien):
        sinh_vien_temp = []
        ten = input(f"nhập tên sinh viên: ")
        sinh_vien_temp.append(ten)
        for j in range(0, so_hoc_phan):
                diem_i = float(input(f"hãy nhập điểm môn:  {j+1}"))
                sinh_vien_temp.append(diem_i)
                
        sinh_vien.append(sinh_vien_temp)
print(sinh_vien)

for i in range(0, so_sinh_vien):
        tong_diem = 0
        for j in range(1, so_hoc_phan + 1):
                tong_diem = tong_diem + sinh_vien[i][j]
        print(f"Điểm TB sinh viên{sinh_vien[i][0]} là: ", tong_diem / so_hoc_phan)
