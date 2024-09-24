# #cách 1: dùng vòng lặp:
# drink = ['Trà chanh', 10000, 'Trà đào', 10000, 'cà phê', 15000, 'nước cam', 15000, 'sữa chua', 25000]

# print("Menu:")
# for i in range(0, len(drink), 2):
#     print(f"{drink[i]}: {drink[i+1]}vnđ")
# print("mời bạn chọn đồ uống: ")
# for i in range(0,10,2):
#     print(f"({int((i+2)/2)}) {drink[i]}")

# oder = int(input("Chọn: "))
# if 1 <= oder <=5:
#     soluong = int(input("nhập số lượng bạn muốn oder: "))
    
#     print(f"{drink[(oder-1)*2]} Giá tiền: {drink[(oder-1)*2+1]}")
#     print(f"số lượng: {soluong} x {drink[(oder-1)*2+1]}")
#     print(f"tổng tiền: {soluong * drink[((oder-1)*2+1)]}")

drink = ['Trà chanh', 10000, 'Trà đào', 10000, 'cà phê', 15000, 'nước cam', 15000, 'sữa chua', 25000]

print("Menu:")
for i in range(0, 10, 2):
    print(f"{drink[i]}: {drink[i+1]}vnđ")
oder = input("mời bạn chọn đồ uống: ")
check = 0
for i in range(0, 10, 2):
    if(oder == drink[i]):
        soluong = int(input("Nhập số lượng: "))
        giatien = soluong * drink[i+1]
        print(f"bạn đã mua: {soluong}x {drink[i]}, bạn phải trả: {giatien}vnđ")
        check = 1
if(check == 0):
    print("xin lỗi đồ bạn gọi không có trong menu")    



# #cách 2: dùng if else
# tra_chanh = 10000
# tra_dao = 10000
# ca_phe = 15000
# nuoc_cam = 15000
# sua_chua = 25000

# print("Menu:")
# print("1. Trà chanh :",tra_chanh,"VNĐ")
# print("2. Trà đào :",tra_dao,"VNĐ")
# print("3. Cà phê :",ca_phe,"VNĐ")
# print("4. Nước cam :",nuoc_cam, "VNĐ")
# print("5. Sữa chua :",sua_chua, "VNĐ")

# nguoi_dung_chon = int(input("Chọn một loại đồ uống(1,2,3,4,5): "))
# soluong = int(input("nhập số lượng bạn muốn oder: "))

# if nguoi_dung_chon == 1:
#     gia_tien = tra_chanh * soluong
#     print("Hoá đơn của bạn:")
#     print(f"Trà Chanh x{soluong}: {gia_tien} VNĐ")
# else:
#     if nguoi_dung_chon == 2:
#         gia_tien = tra_dao * soluong
#         print("Hoá đơn của bạn:")
#         print(f"Trà đào x{soluong}: {gia_tien} VNĐ")
#     else:
#         if nguoi_dung_chon == 3 :
#             gia_tien = ca_phe * soluong
#             print("Hoá đơn của bạn:")
#             print(f"Cà phê x{soluong}: {gia_tien} VNĐ")
#         else:
#             if nguoi_dung_chon == 4:
#                 gia_tien = nuoc_cam * soluong
#                 print("Hoá đơn của bạn:")
#                 print(f"Nước cam x{soluong}: {gia_tien} VNĐ")
#             else:
#                 if nguoi_dung_chon == 5:
#                     gia_tien = sua_chua * soluong
#                     print("Hoá đơn của bạn:")
#                     print(f"Sữa chua x{soluong}: {gia_tien} VNĐ")
#                 else:
#                     print("đồ bạn gọi không có trong menu")


# #cách 3: dùng if, elif và else
# tra_chanh = 10000
# tra_dao = 10000
# ca_phe = 15000
# nuoc_cam = 15000
# sua_chua = 25000

# print("Menu:")
# print("1. Trà chanh :",tra_chanh,"VNĐ")
# print("2. Trà đào :",tra_dao,"VNĐ")
# print("3. Cà phê :",ca_phe,"VNĐ")
# print("4. Nước cam :",nuoc_cam, "VNĐ")
# print("5. Sữa chua :",sua_chua, "VNĐ")

# nguoi_dung_chon = int(input("Chọn một loại đồ uống(1,2,3,4,5): "))
# soluong = int(input("nhập số lượng bạn muốn oder: "))

# if nguoi_dung_chon == 1:
#     gia_tien = tra_chanh * soluong
#     print("Hoá đơn của bạn:")
#     print(f"Trà Chanh x{soluong}: {gia_tien} VNĐ")
# elif nguoi_dung_chon == 2:
#     gia_tien = tra_dao * soluong
#     print("Hoá đơn của bạn:")
#     print(f"Trà đào x{soluong}: {gia_tien} VNĐ")
# elif nguoi_dung_chon == 3 :
#     gia_tien = ca_phe * soluong
#     print("Hoá đơn của bạn:")
#     print(f"Cà phê x{soluong}: {gia_tien} VNĐ")
# elif nguoi_dung_chon == 4:
#     gia_tien = nuoc_cam * soluong
#     print("Hoá đơn của bạn:")
#     print(f"Nước cam x{soluong}: {gia_tien} VNĐ")
# elif nguoi_dung_chon == 5:
#     gia_tien = sua_chua * soluong
#     print("Hoá đơn của bạn:")
#     print(f"Sữa chua x{soluong}: {gia_tien} VNĐ")
# else:
#     print("đồ bạn gọi không có trong menu")