from datetime import datetime

def total_days_from_start_of_year(day, month, year):
    try:
        start_of_year = datetime(year, 1, 1)
        end_date = datetime(year, month, day)
        days_difference = (end_date - start_of_year).days + 1
        return days_difference
    except ValueError:
        return None

# Nhập dữ liệu từ người dùng
day = int(input("Nhập ngày: "))
month = int(input("Nhập tháng: "))
year = int(input("Nhập năm: "))

result = total_days_from_start_of_year(day, month, year)

if result is not None:
    print(f"Tổng số ngày từ đầu năm đến ngày {day}/{month}/{year} là: {result} ngày.")
else:
    print("Ngày tháng năm không hợp lệ.")
