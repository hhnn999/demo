from so_chinh_phuong import tim_so_chinh_phuong_nho_nhat

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        so_luong_phan_tu = int(f.readline())
        day_so = list(map(int, f.readline().split()))
    
    ket_qua = tim_so_chinh_phuong_nho_nhat(day_so)

    with open("output.txt", "w") as f:
        f.write(str(ket_qua))
    