from prettytable import PrettyTable

class SinhVien:
    def __init__(self, ho_ten, diem_tin, diem_c):
        self.ho_ten = ho_ten
        self.diem_tin = diem_tin
        self.diem_c = diem_c

danh_sach_sv = []

while True:
    ho_ten = input("Nhập họ tên SV (Nhập xâu rỗng để kết thúc): ")
    
    if not ho_ten:
        break

    diem_tin = float(input("Nhập điểm Tin đại cương: "))
    diem_c = float(input("Nhập điểm LT C: "))

    sv = SinhVien(ho_ten, diem_tin, diem_c)
    danh_sach_sv.append(sv)

# Tạo bảng
table = PrettyTable()
table.field_names = ["Họ tên", "Tin học Đại cương", "LT C"]

# Thêm dữ liệu vào bảng
for sv in danh_sach_sv:
    table.add_row([sv.ho_ten, sv.diem_tin, sv.diem_c])

print(table)
