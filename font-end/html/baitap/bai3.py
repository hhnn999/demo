from datetime import datetime

def days_in_date(day, month, year):
    try:
        date_str = f"{year}-{month}-{day}"
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        days = (date_obj - datetime(date_obj.year, 1, 1)).days + 1
        return days
    except ValueError:
        return None

# Nhập dữ liệu từ người dùng
day = int(input("Nhập ngày: "))
month = int(input("Nhập tháng: "))
year = int(input("Nhập năm: "))

result = days_in_date(day, month, year)

if result is not None:
    print(f"Số ngày của ngày {day}/{month}/{year} là: {result}")
else:
    print("Ngày tháng năm không hợp lệ.")
