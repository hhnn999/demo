# cách 1: dùng if
nhapso = int(input("nhập vào một số: "))
if(1 <= nhapso <= 10):
    print("giá trị bình phương của số vừa nhập là: ",nhapso * nhapso) 
if(nhapso < 1):
    print("bạn đã nhập sai")
if (nhapso > 10):
    print("bạn đã nhập sai")
    
    
# cách 2: dùng if else
nhapso = int(input("nhập vào một số: "))
if(1 <= nhapso <= 10):
    print("giá trị bình phương của số vừa nhập là: ", nhapso * nhapso)
else:
    print("bạn đã nhập sai")
    
    
#cách 3: dùng if, elif và else
nhapso = int(input("nhập vào một số: "))
if(nhapso < 1):
    print("bạn đã nhập sai")
elif(nhapso > 10):
    print("bạn đã nhập sai")
else:
    print("giá trị bình phương của số vừa nhập là: ",nhapso * nhapso)   