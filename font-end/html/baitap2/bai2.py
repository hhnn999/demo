from module_baitap import nhan2matran, matranchuyenvi, cong2matran

matrix_a = [
    [1, 2],
    [4, 5],
]

matrix_b = [
    [7, 8],
    [9, 10],
]

ketqua_nhan = nhan2matran(matrix_a, matrix_b)
ketqua_chuyenvi = matranchuyenvi(matrix_a)
ketqua_cong = cong2matran(matrix_a, matrix_b)

print("Kết quả nhân hai ma trận:")
print(ketqua_nhan)

print("Kết quả chuyển vị ma trận:")
print(ketqua_chuyenvi)

print("Kết quả cộng hai ma trận:")
print(ketqua_cong)
