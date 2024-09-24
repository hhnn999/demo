def merge_and_remove_duplicates(list1, list2):
    # Kết hợp hai danh sách
    merged_list = list1 + list2

    # Sử dụng set để loại bỏ các giá trị trùng lặp và giữ lại chỉ một lần
    unique_list = list(set(merged_list))

    return unique_list

# Ví dụ sử dụng:
A = [1, 2, 3, 4, 5]
B = [3, 4, 5, 6, 7]
result = merge_and_remove_duplicates(A, B)
print(result)
