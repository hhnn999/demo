import module_baitap
print("phương trình bậc 1: ax + b = 0")
a = int(input("nhập a: "))
b = int(input("nhập b: "))

if(a == 0 and b == 0):
    print("phương trình vô số nghiệm")
elif(a == 0 and b > 0 and b < 0):
    print("phương trình vô nghiệm")
elif(a  > 0 or a < 0):
    print("phương trình có nghiệm duy nhất là: ", module_baitap.bac1(a,b))