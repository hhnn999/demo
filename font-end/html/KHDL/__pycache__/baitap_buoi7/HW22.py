so_sinh_vien = int(input("nhập vào số sinh viên: "))
danh_sach_chieu_cao = []

for i in range(0, so_sinh_vien):
    nhap_chieu_cao = float(input(f"nhập vào chiều cao (m) của sinh viên thứ {i+1}: "))
    danh_sach_chieu_cao.append(nhap_chieu_cao)

sv_cao_nhat = danh_sach_chieu_cao[0]
sv_thap_nhat = danh_sach_chieu_cao[0]

for i in range(0, len(danh_sach_chieu_cao)):
    chieu_cao = danh_sach_chieu_cao[i]
    if chieu_cao > sv_cao_nhat:
        sv_cao_nhat = chieu_cao
    elif chieu_cao < sv_thap_nhat:
        sv_thap_nhat = chieu_cao
        
tong_chieu_cao = 0        
for i in danh_sach_chieu_cao:
    tong_chieu_cao = tong_chieu_cao + i
    
dem = 0
for j in range(len(danh_sach_chieu_cao)):
    if danh_sach_chieu_cao[j] >= tong_chieu_cao / so_sinh_vien:
         dem = dem + 1
      
print(f"sinh viên cao nhất: {sv_cao_nhat} (m)")
print(f"sinh viên thấp nhất: {sv_thap_nhat} (m)")
print(f"chiều cao trung bình của sinh viên trong lớp: {tong_chieu_cao / so_sinh_vien:.2f} (m)")
print(f"số sinh viên trong lớp có chiều cao >= chiều cao TB là: {dem}")