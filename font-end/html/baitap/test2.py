input_string = input("Nhập chuỗi: ")

kytu_count = len(input_string)
print(f"Số ký tự trong chuỗi là: {kytu_count}")

so_count = 0
for char in input_string: 
    if char.isdigit():
        so_count += 1
print(f"Số chữ số trong chuỗi là: {so_count}")

c = 0
for char in input_string:
    if not char.isdigit() and not char.isspace():
        c += 1
print("Số ký tự không phải là chữ số và không phải là chữ cái tiếng anh là: ", c)