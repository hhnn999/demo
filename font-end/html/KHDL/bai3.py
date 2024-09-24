thong_tin_sinh_vien = [
    {"ten": "Hoàng", "nganh": "CNTT"},
    {"ten": "Hải", "nganh": "CNTT"},
    {"ten": "Toàn", "nganh": "QTKD"},
    {"ten": "Hoa", "nganh": "QTKD"},
    {"ten": "Huy", "nganh": "CNTT"},
    {"ten": "Minh", "nganh": "CNTT"},
    {"ten": "Giang", "nganh": "CNTT"},
    {"ten": "Huyền", "nganh": "QTKD"}
]

for i in thong_tin_sinh_vien:
    if (i['nganh'] == 'CNTT'):
        print(f"sinh viên ngành CNTT: {i['ten']}")
    elif(i['nganh'] == 'QTKD'):
        print(f"sinh viên ngành QTKD: {i['ten']}")

sv_nganh_CNTT = 0
sv_nganh_QTKD = 0


for ban in thong_tin_sinh_vien:
    if ban["nganh"] == "CNTT":
        sv_nganh_CNTT += 1
    elif ban["nganh"] == "QTKD":
        sv_nganh_QTKD += 1

print(f"Số lượng sv cntt trong lớp: {sv_nganh_CNTT}")
print(f"Số lượng sv qtkd trong lớp: {sv_nganh_QTKD}")