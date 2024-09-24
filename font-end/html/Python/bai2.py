def tron_xau(s1, s2):
    result = []
    i, j = 0, 0

    while i < len(s1) and j < len(s2):
        result.append(s1[i])
        result.append(s2[j])
        i += 1
        j += 1

    # Nếu một trong hai xâu kết thúc, thêm các phần còn lại của xâu kia vào kết quả
    while i < len(s1):
        result.append(s1[i])
        i += 1

    while j < len(s2):
        result.append(s2[j])
        j += 1

    return result

s1 = input("Nhập xâu s1: ")
s2 = input("Nhập xâu s2: ")

# Chuyển xâu nhập thành danh sách kí tự
s1_list = list(s1)
s2_list = list(s2)

result_list = tron_xau(s1_list, s2_list)
print(f"Kết quả: {result_list}")
