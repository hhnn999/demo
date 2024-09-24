def tim_so_chinh_phuong_nho_nhat(day_so):
    gia_tri_lon_nhat = max(day_so)
    p = gia_tri_lon_nhat
    while True:
        co_the_chia_het = all(p % num == 0 for num in day_so)
        if co_the_chia_het and (p ** 0.5).is_integer():
            return p % (10**9 + 7)
        p += gia_tri_lon_nhat

if __name__ == "__main__":
    so_luong_phan_tu = int(input())
    day_so = list(map(int, input().split()))
    ket_qua = tim_so_chinh_phuong_nho_nhat(day_so)
    print(ket_qua)
