# Hàm đếm số phần tử của một danh sách
def dem_so_phan_tu(danh_sach):
    dem = 0
    for i in danh_sach:
        dem = dem + 1
    return dem
list = [1,7,4,6,8,3,6,9]

check = dem_so_phan_tu(list)
print(list)
print("Số phần tử trong danh sách là:", check)
print("---------------------------------")

# Hàm kiểm tra giá trị nhập vào
def kiem_tra(gia_tri, gia_tri_nho_nhat, gia_tri_lon_nhat ):
    if (gia_tri_nho_nhat <= gia_tri <= gia_tri_lon_nhat):
        return gia_tri
    else: 
        return 0
nhap_gia_tri = int(input("Nhập số trong khoảng từ 0 -> 10: "))
nhap_gia_tri = kiem_tra(nhap_gia_tri, 0, 10)
print(f"Đúng trả về giá trị nhập, 0 là sai:\nReturn: {nhap_gia_tri}")
print(f"---------------------------------------")

# Hàm sắp xếp từ bé đến lớn
mang = [1, 0, 5, 3, 8, 2, 6, 7, 8, 4, 9]
print(mang)
def sap_xep(mang):
    for i in range(0,len(mang)):
        for j in range(i+1,len(mang)):
            if(mang[i] > mang[j]):
                temp = mang[i]
                mang[i] = mang[j]
                mang[j] = temp
    return mang

mang = sap_xep(mang)
print(f"Sắp xép tăng: ")
print(f"{mang}")
print(f"---------------------------------------")

# Hàm sắp xếp từ lớn đến bé
def sap_xep(mang):
    for i in range(0,len(mang)):
        for j in range(i+1,len(mang)):
            if(mang[i] < mang[j]):
                temp = mang[j]
                mang[j] = mang[i]
                mang[i] = temp
    return mang

mang = [1, 0, 5, 3, 8, 2, 6, 7, 8, 4, 9]
mang = sap_xep(mang)
print(f"Sắp xép giảm: ")
print(f"{mang}")