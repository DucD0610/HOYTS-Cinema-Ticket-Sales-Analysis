import random

x = random.randint(1,100)
print(f"Generated a random number from 1 to 100: {x}")

if x % 2 == 0:
    print ("This is even number")
else:
    print ("This is odd number")

# prompt: Cho một chuỗi ký tự s = 'Hello world!'. Hãy in ra màn hình các thông tin như sau:
# 3 ký tự đầu tiên của chuỗi
# Các ký tự từ index số 3 cho tới index số 7
# Kiểm tra xem có tồn tại ký tự 'w' ở trong chuỗi hay không, nếu có hãy in ra màn hình dòng chữ: "Tồn tại ký tự w ở trong chuỗi"

s = 'Hello world!'

# 3 ký tự đầu tiên của chuỗi
print(s[:3])

# Các ký tự từ index số 3 cho tới index số 7
print(s[3:8])

# Kiểm tra xem có tồn tại ký tự 'w' ở trong chuỗi hay không
if 'w' in s:
  print("Tồn tại ký tự w ở trong chuỗi")
  
  
# prompt: Thêm vào list_1 phần tử có giá trị 50 vào cuối list
# Cập nhật giá trị phần tử tại index 2 của list_2 với giá trị là: 100
# In ra màn hình tích của phần tử đầu tiên của list_1 với phần tử cuối cùng của list_2
# Trả về kết quả tổng của 2 list con:
# Danh sách con đầu tiên: trích xuất các phần tử của list_1 từ vị trí index 2 cho tới index 4
# Danh sách con thứ hai: trích xuất các phần tử của list_2 từ index 3 cho tới phần tử cuối cùng

list_1 = [1, 2, 3, 4, 5]
list_2 = [6, 7, 8, 9, 10]

# Thêm vào list_1 phần tử có giá trị 50 vào cuối list
list_1.append(50)

# Cập nhật giá trị phần tử tại index 2 của list_2 với giá trị là: 100
list_2[2] = 100

# In ra màn hình tích của phần tử đầu tiên của list_1 với phần tử cuối cùng của list_2
print(list_1[0] * list_2[-1])

# Trả về kết quả tổng của 2 list con:
# Danh sách con đầu tiên: trích xuất các phần tử của list_1 từ vị trí index 2 cho tới index 4
# Danh sách con thứ hai: trích xuất các phần tử của list_2 từ index 3 cho tới phần tử cuối cùng
list_con_1 = list_1[2:5]
list_con_2 = list_2[3:]

tong_2_list_con = sum(list_con_1) + sum(list_con_2)
tong_2_list_con

# prompt: Bài tập 4: Cho một biến có tên là year thể hiện năm. Hãy in ra màn hình dòng chữ: "Năm đó là năm nhuận" nếu year là năm nhuận, ngược lại thì in ra: "Năm đó không phải là năm nhuận".
# ! Lưu ý: những năm nào chia hết cho 4 được và không chia hết cho 100 được coi là năm nhuận (ví dụ năm 2100 không phải là năm nhuận, 2104 là năm nhuận), nếu kết quả chia hết cho 400 thì năm đó là năm nhuận

year = 2024  # Thay đổi giá trị year để kiểm tra

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
  print("Năm đó là năm nhuận")
else:
  print("Năm đó không phải là năm nhuận")
  
# Bài tập 5: Cho 1 dãy số các số nguyên bất kỳ, in ra số lượng các số chẵn, số lượng các số lẽ xuất hiện trong dãy
import random

numbers = [random.randint(-100, 100) for _ in range(20)]  # Tạo một danh sách 20 số nguyên ngẫu nhiên
print(f"Danh sách số nguyên: {numbers}")

even_count = 0
odd_count = 0

for number in numbers:
  if number % 2 == 0:
    even_count += 1
  else:
    odd_count += 1

print(f"Số lượng số chẵn: {even_count}")
print(f"Số lượng số lẻ: {odd_count}")

# Bài tập 6: Cho một chuỗi ký tự bất kỳ (bao gồm: ‘A’->’Z’,’a’-> ‘z’). Đếm trong chuỗi đó có bao nhiêu ký tự in hoa, bao nhiêu ký tự in thường?

string = "Hello World! This Is A Test String."

upper_count = 0
lower_count = 0

for char in string:
  if 'A' <= char <= 'Z':
    upper_count += 1
  elif 'a' <= char <= 'z':
    lower_count += 1

print(f"Số ký tự in hoa: {upper_count}")
print(f"Số ký tự in thường: {lower_count}")

#Bài tập 7: Cho một số nguyên dương a bất kỳ (a nằm trong đoạn [0,1000]). Liệt kê tất các bội số của a nằm trong đoạn [0,1000]


# Bài tập 8: Tìm giá trị lớn nhất và giá trị nhỏ nhất xuất hiện trong dãy số bất kỳ
import random

numbers = [random.randint(-100, 100) for _ in range(20)]  # Tạo một danh sách 20 số nguyên ngẫu nhiên
print(f"Danh sách số nguyên: {numbers}")

if not numbers:
  print("Danh sách rỗng, không có giá trị lớn nhất và nhỏ nhất.")
else:
  max_number = numbers[0]
  min_number = numbers[0]

  for number in numbers:
    if number > max_number:
      max_number = number
    if number < min_number:
      min_number = number

  print(f"Giá trị lớn nhất: {max_number}")
  print(f"Giá trị nhỏ nhất: {min_number}")

#Bài tập 9: Xây dựng 1 hàm dùng để kiểm tra 1 số nguyên dương có phải là số nguyên tố hay không. Sau đó cho 1 danh sách các số nguyên bất kỳ, hãy tính tổng các số nguyên tố có trong dãy số

def is_prime(n):
  """Kiểm tra xem một số nguyên dương có phải là số nguyên tố hay không."""
  if n <= 1:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True


def sum_primes_in_list(numbers):
  """Tính tổng các số nguyên tố trong một danh sách số nguyên."""
  sum_primes = 0
  for number in numbers:
    if is_prime(number):
      sum_primes += number
  return sum_primes


# Ví dụ sử dụng:
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
sum_of_primes = sum_primes_in_list(numbers)
print(f"Tổng các số nguyên tố trong danh sách {numbers} là: {sum_of_primes}")

#Bai tap 9: Xây dựng 1 hàm để kiểm tra 1 password có phải là 1 password hợp lệ hay không. Sau đó cho 1 danh sách password bất kỳ, hãy đếm số lượng password hợp lệ có trong dãy số đó.
# Một password hợp lệ khi và chỉ khi thỏa mãn tất cả các điều kiện sau:
# Ít nhất 1 chữ cái nằm trong [a-z]
# Ít nhất 1 số nằm trong [0-9]
# Ít nhất 1 kí tự nằm trong [A-Z]
# Ít nhất 1 ký tự nằm trong [$ # @]
# Độ dài mật khẩu tối thiểu: 6
# Độ dài mật khẩu tối đa: 12

import re

def is_valid_password(password):
  """Kiểm tra xem một mật khẩu có hợp lệ hay không."""
  if not (6 <= len(password) <= 12):
    return False
  if not re.search("[a-z]", password):
    return False
  if not re.search("[0-9]", password):
    return False
  if not re.search("[A-Z]", password):
    return False
  if not re.search("[$#@]", password):
    return False
  return True


def count_valid_passwords(passwords):
  """Đếm số lượng mật khẩu hợp lệ trong một danh sách."""
  count = 0
  for password in passwords:
    if is_valid_password(password):
      count += 1
  return count


# Ví dụ sử dụng:
passwords = ["Password123", "weakpass", "StrongPass$1", "PasswOrd", "pass1234567890", "PasswOrd@123"]
valid_password_count = count_valid_passwords(passwords)
print(f"Số lượng mật khẩu hợp lệ trong danh sách là: {valid_password_count}")