so_sv = int(input(f'Nhập vào số lượng sinh viên: '))
so_hp = int(input(f'Nhập vào số lượng học phần: '))

ds_hp = []

for i in range(0,so_hp):
    ds_hp.append(input(f"Nhập vào tên môn học số {i+1}: "))
ds_sv = []
for i in range(so_sv):
    sinh_vien = {}
    sinh_vien['id'] = input(f"Nhập vào ID sinh viên {i+1}: ")
    sinh_vien['ten'] = input(f"Nhập vào tên sinh viên {i+1}: ")
    diem_hp = {}
    for hoc_phan in ds_hp:
        diem_hp[hoc_phan] = float(input(f"Nhập vào điểm học phần {hoc_phan}: "))
    sinh_vien['diem'] = diem_hp
    # print(f"diem hp{diem_hp}")
    ds_sv.append(sinh_vien)
    # print(f"ds sv{ds_sv}")
for sv in ds_sv:
    diem_tb = 0
    for diem in sv['diem']:
        diem_tb += sv['diem'][diem]
    print(f"-------------------------")
    print(f"ID: {sv['id']}")
    print(f"Tên sinh viên: {sv['ten']}")
    print(f"Điểm học phần: ")
    for ten_mh, diem_mh in sv['diem'].items():
        print(f"{ten_mh}: {diem_mh}")
    print(f"Điểm trung bình: {diem_tb/so_hp}")
    
