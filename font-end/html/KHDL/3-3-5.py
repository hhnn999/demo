diemtrungtuyen = ['CNTTCLC', 22, 'CNTT', 18, 'KHDL', 18, 'DIACHAT', 18, 'MOITRUONG', 15]
diem_toan = float(input("nhập điểm toán: "))
diem_ly = float(input("nhập điểm lý: "))
diem_hoa = float(input("nhập điểm hoá: "))
tongdiem = diem_toan + diem_ly + diem_hoa

check = 0
for i in range(1,len(diemtrungtuyen),2):
    if (tongdiem >= diemtrungtuyen[i]):
        print(f"bạn đã trúng tuyển ngành: {diemtrungtuyen[i-1]}")
        check = 1
if check == 0:
    print("bạn đã trượt")






# diem_toan = int(input("nhập điểm toán: "))
# diem_ly = int(input("nhập điểm lý: "))
# diem_hoa = int(input("nhập điểm hoá: "))

# tongdiem = diem_toan + diem_ly + diem_hoa

# CNTT = 18
# CNTTCLC = 22
# KHDL = 18
# DIACHAT = 17
# MOITRUONG = 15

# if(tongdiem >= 22):
#     print(f"chúc mừng bạn đã trúng tuyển các ngành sau: CNTT, KHDL, CNTTCLC, DIACHAT, MOITRUONG")
# elif(tongdiem >= 18):
#     print(f"chúc mừng bạn đã trúng tuyển các ngành sau: CNTT, KHDL")
# elif(tongdiem >= 17):
#     print(f"chúc mừng bạn đã trúng tuyển các ngành sau: Địa chất")  
# elif(tongdiem >= 15):
#     print(f"chúc mừng bạn đã trúng tuyển các ngành sau: Môi trường")
# else:
#     print("chúc mừng bạn đã trượt hihi =)))")