# cách 2: dùng if else
gioitinh = input("nhập giới tính(nam,nữ): ")
tuoi = int(input("nhập tuổi: "))
namkinhnghiem = float(input("nhập số năm kinh nghiệm: "))
chieucao = float(input("nhập chiều cao(m): "))
cannang = float(input("nhập cân nặng(kg): "))
dieu_kien_1 = gioitinh == "nữ" and 30 < tuoi < 40 and 2 <= namkinhnghiem < 5 and chieucao >= 1.60 and cannang >= 50
dieu_kien_2 = gioitinh == "nữ" and 30 < tuoi < 40 and namkinhnghiem >= 5 and chieucao >= 1.55 and cannang <= 45
dieu_kien_3 = gioitinh == "nữ" and 18 <= tuoi <= 40 and chieucao >= 1.55 and cannang >= 45
if (dieu_kien_1 or dieu_kien_2 or dieu_kien_3):
    print("Xin chúc mừng bạn đã đủ tiêu chuẩn làm việc")
else:
    print("Xin lỗi, chúc bạn may mắn lần sau ^^")

# cách 3: dùng if, elif và else
gioitinh = input("nhập giới tính(nam,nữ): ")
tuoi = int(input("nhập tuổi: "))
namkinhnghiem = float(input("nhập số năm kinh nghiệm: "))
chieucao = float(input("nhập chiều cao(m): "))
cannang = float(input("nhập cân nặng(kg): "))

if (gioitinh == "nữ"):
    if (30 < tuoi < 40):
        if (2 <= namkinhnghiem < 5):
            if (chieucao >= 1.60 and cannang >= 50):
                print("Xin chúc mừng, bạn đã đủ tiêu chuẩn làm việc")
            else:
                print("xin lỗi, chúc bạn may mắn lần sau ^^")
        elif (namkinhnghiem >= 5):
            if (chieucao >= 1.55 and cannang <= 45):
                print("Xin chúc mừng, bạn đã đủ tiêu chuẩn làm việc")
            else:
                print("xin lỗi, chúc bạn may mắn lần sau ^^")    
        else:
            print("xin lỗi, chúc bạn may mắn lần sau ^^")   
    elif (18 <= tuoi <= 40):
        if (chieucao >= 1.55 and cannang <= 45):
            print("Xin chúc mừng, bạn đã đủ tiêu chuẩn làm việc")
        else:
            print("xin lỗi, chúc bạn may mắn lần sau ^^")
    else:
            print("xin lỗi, chúc bạn may mắn lần sau ^^")
else:
    print("xin lỗi, công ty chỉ tuyển phụ nữ =)))))))")    
                                