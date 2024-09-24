a = input('Nhap canh a cua hinh tam giac: ');
b = input('Nhap canh b cua hinh tam giac: ');
c = input('Nhap canh c cua hinh tam giac: ');

p = (a+b+c)/2;
S = sqrt(p*(p-a)*(p-b)*(p-c));

fprintf('dien tich hinh tam giac la: %.2f\n', S');