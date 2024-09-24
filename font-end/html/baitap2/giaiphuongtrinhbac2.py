from module_baitap import*
print("phương trình bậc 2: ax*x + bx + c = 0")
a = int(input("nhập a: "))
b = int(input("nhập b: "))
c = int(input("nhập c: "))

if delta(a,b,c) < 0:
    print("phương trình vô nghiệm")
elif delta(a,b,c) == 0:
    print("phương trình có nghiệm kép là: x1 = x2 =", nghiemkep(a,b))
elif delta(a,b,c) > 0:
    print(f"phương trình có 2 nghiệm phân biệt là: x1 = {x1(a,b,delta(a,b,c))}, x2 = {x2(a,b,delta(a,b,c))}")