#cách 1: dùng if
import turtle
hoang = turtle.Turtle()

hinh_can_ve = input("Nhập hình muốn vẽ (hình tròn / hình vuông / hình tam giác): ")    
if hinh_can_ve == "hình tròn":
    ban_kinh = float(input("Nhập bán kính của hình tròn: "))
    hoang.circle(ban_kinh)

if hinh_can_ve == "hình vuông":
    kich_thuoc = float(input("Nhập kích thước của hình vuông: "))
    hoang.forward(kich_thuoc)
    hoang.left(90)
    hoang.forward(kich_thuoc)
    hoang.left(90)
    hoang.forward(kich_thuoc)
    hoang.left(90)
    hoang.forward(kich_thuoc)
    hoang.left(90)
        
if hinh_can_ve == "hình tam giác":
    kich_thuoc = float(input("Nhập kích thước của hình tam giác: "))
    hoang.forward(kich_thuoc)
    hoang.left(120)
    hoang.forward(kich_thuoc)
    hoang.left(120)
    hoang.forward(kich_thuoc)
    hoang.left(120)

if (hinh_can_ve != "hình tam giác" and hinh_can_ve != "hình vuông" and hinh_can_ve != "hình tròn"):
    print("hình bạn nhập không được hỗ trợ")


#cách 2: dùng if else
import turtle
hoang = turtle.Turtle()

hinh_can_ve = input("Nhập hình muốn vẽ (hình tròn / hình vuông / hình tam giác): ")    
if hinh_can_ve == "hình tròn":
    ban_kinh = float(input("Nhập bán kính của hình tròn: "))
    hoang.circle(ban_kinh)
else:
    if hinh_can_ve == "hình vuông":
        kich_thuoc = float(input("Nhập kích thước của hình vuông: "))
        hoang.forward(kich_thuoc)
        hoang.left(90)
        hoang.forward(kich_thuoc)
        hoang.left(90)
        hoang.forward(kich_thuoc)
        hoang.left(90)
        hoang.forward(kich_thuoc)
        hoang.left(90)
    else:
        if hinh_can_ve == "hình tam giác":
            kich_thuoc = float(input("Nhập kích thước của hình tam giác: "))
            hoang.forward(kich_thuoc)
            hoang.left(120)
            hoang.forward(kich_thuoc)
            hoang.left(120)
            hoang.forward(kich_thuoc)
            hoang.left(120)
        else:
            print("hình bạn nhập không được hỗ trợ")
    
    
#cách 3: dùng if, elif và else
import turtle
hoang = turtle.Turtle()

hinh_can_ve = input("Nhập hình muốn vẽ (hình tròn / hình vuông / hình tam giác): ")    
if hinh_can_ve == "hình tròn":
    ban_kinh = float(input("Nhập bán kính của hình tròn: "))
    hoang.circle(ban_kinh)

elif hinh_can_ve == "hình vuông":
        kich_thuoc = float(input("Nhập kích thước của hình vuông: "))
        hoang.forward(kich_thuoc)
        hoang.left(90)
        hoang.forward(kich_thuoc)
        hoang.left(90)
        hoang.forward(kich_thuoc)
        hoang.left(90)
        hoang.forward(kich_thuoc)
        hoang.left(90)
        
elif hinh_can_ve == "hình tam giác":
            kich_thuoc = float(input("Nhập kích thước của hình tam giác: "))
            hoang.forward(kich_thuoc)
            hoang.left(120)
            hoang.forward(kich_thuoc)
            hoang.left(120)
            hoang.forward(kich_thuoc)
            hoang.left(120)

else:
    print("hình bạn nhập không được hỗ trợ")
    