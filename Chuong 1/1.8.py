# 1.7 nhập và xuất trong java
    #format()
name = "Vũ Hữu Tuấn"
msv = "2321050018"
lop = "DCCTCT68_09"
truong = "Đại học Mỏ - Địa chất"
print("Xin chào tôi tên là {}, msv là {}, lớp là {} , là sinh viên trường {}".format(name,msv,lop,truong))

# các kiểu dữ liệu chuẩn trong python
# các hàm xử lý xâu
# Bài tập : nhập vào 1 xâu "CcnTt dia tin hoc,dia chat". Hiển thị xâu đó từ vị trí 3,4-7 và tất cả
s ="CcnTt dia tin hoc,dia chat"
print(s[3])  # lấy ra ký tự T
print(s[4:8]) # lấy ra ký tự t di
print(s[:]) # lấy ra hết xâu
print(s[0:]) # lấy ra hết xâu
print(s[4:2:-1]) # lấy ra tT
print(s[-1:-3:-1]) # lấy ra ta
print(s[-3:-1]) # lấy ra ha
#  xuất
print('a' in "abc") #kiểm tra xem ký tự a có trong xâu "abc" hay ko nếu có trả về true còn ko thì trả về false
# Các hàm
#  hàm len()
a="dia"
print(len(a)) # trả về số lượng ký tự có trong chuỗi
# hàm lower(), upper()
print(a.lower())
print(a.upper())
#  hàm find() -> hàm tìm vị trí cảu ký tự có trong chuỗi
print(s.find(a))
print(s.find(a, 10))
print(s.find(a, 20))

#  count() -> hàm đếm
print(s.count(a))
print(s.count(a,10))
print(s.count(a,10, -1))

#replace() -> thay thế
print(s.replace("dia", "địa"))
print(s.replace("dia", "địa", 2))

#split()
print(s.split())
print(s.split(" ", 1))

#lstrip(), rstrip(), strip()
s1 = "   dia hoc   "
print(s1.lstrip())
print(s1.rstrip())
print(s1.strip())

#isalpha(), isdigit(), isspace()
print("abc".isalpha())
print("ab c".isalpha())
print("123".isdigit())
print("12 3".isdigit())
print("   ".isspace())
print(" .  ".isspace())

#1.8.3 List
#Các hàm tương tự như xâu: len(), count(), index(), find(), in, replace(), split(),append(), insert(), pop(), remove(), sort(), reverse(),...
#hàm list(): chuyển 1 tuple thành list:
t = (1, "a1", "abc")
l = list(t)
print(t)
print(l)

#toán tử +,*:
l1 = [1, 2, 3]
l2 = [4, 5, 6]
print(l1 + l2)
print(l1 * 3)
l3 = [1, "ab", [1, 2]]
l4 = [1, "cd", [3,4]]
print(l3 + l4)

#print(l3 * l4) #ko dc
print(["ab"] * 2)
#thay đổi phần tử trong list:
l5 = [1, 2, 3, 4]
l5[0] = 10
print(l5)

#thay đổi phần tử trong list con:
l6 = [1, 2, [3, 4]]
l6[2][0] = 30
print(l6)

#hàm len():
l7 = [1, 2, 3, 4]
print(len(l7))
l8 = [1, 2, [3, 4]]
print(len(l8))

#max, min:
l9 = [1, 2, 3, 4]
print(max(l9))
print(min(l9))

#append():
l10 = [1, 2, 3]
l10.append(4)
print(l10)

#count():
l11 = [1, 2, 3, 2, 4]
print(l11.count(2))

#extend():
l12 = [1, 2, 3]
l13 = [4, 5, 6]
l12.extend(l13)
print(l12)

#index():
l14 = [1, 2, 3, 2, 4]
print(l14.index(2))
print(l14.index(2, 2))

#insert():
l15 = [1, 2, 3]
l15.insert(1, 10)
print(l15)

#pop():
l16 = [1, 2, 3, 4]
print(l16.pop()) #mặc định xóa phần tử cuối
print(l16)

#remove():
l17 = [1, 2, 3, 2, 4]
l17.remove(2) #xóa phần tử đầu tiên có giá trị 2
print(l17)

#del():
l18 = [1, 2, 3, 4]
del l18[1] #xóa phần tử có vị trí 1
print(l18)

#reverse():
l19 = [1, 2, 3, 4]
l19.reverse()
print(l19)

#clear():
l20 = [1, 2, 3, 4]
l20.clear()
print(l20)

#sort():
l21 = [3, 1, 4, 2]
l21.sort()
print(l21)

#list chứa list:
l22 = [[1, 2,3], [4, 5, 6]]
print(l22)
print(l22[0])
print(l22[0][1])
print(l22[0][:2])
print(l22[0][:])

#Bài tập:
#Nhập vào 1 chuỗi số cách nhau bởi " ", chuyển chúng thành list số nguyên và tính tổng.In ra ma trận 1 chiều của chuỗi số đó
s1 = input("Nhập vào một chuỗi số cách nhau bởi khoảng trắng: ")
lst = eval("[" + s1.replace(" ",",") + "]") #chuyển chuỗi thành list
print(lst)
s2 = input("Nhập vào một chuỗi số cách nhau bởi dấu phẩy và các hàng của ma trận cách nhau bởi dấu chấm phẩy: ")
matran = eval("[" + s2.replace(";","],[").replace(" ",",") + "]")
#s2 = "1 2 3;4 5 6;7 8 9" sao không nhập vào chuỗi số cách nhau bởi dấu phẩy và các hàng của ma trận cách nhau bởi dấu chấm phẩy, do
print(matran)
tong = sum(lst)
print(tong)

#1.8.4 Tuple
#BT: Nhập matran 4x3 dưới dạng tuple:
s3 = input("Nhập vào một chuỗi số cách nhau bởi dấu phẩy và các hàng của ma trận cách nhau bởi dấu chấm phẩy: ")
matran_tuple = eval("(" + s3.replace(";","),(").replace(" ",",") + ")")
print(matran_tuple)


#in phần tử của tuple, cách nhau bởi " ", sử dụng *matrix[]:
print(*matran_tuple)

#1.8.5. Dictionary
dic = {"name": "Trần Công Hùng", "msv": "2321050068", "lop": "DCCTCT68B"}
print(dic)
print(dic["name"])
dic["cannang"] = 60
print(dic)

#1.8.6 Date and Time
import datetime
#lấy ngày giờ hiện tại:
now = datetime.datetime.now()
print(now)
#tạo một đối tượng datetime:
dt = datetime.datetime(2024, 6, 1, 12, 0, 0)
print(dt)
#pthuc strftime(): định dạng ngày giờ thành chuỗi:
import datetime
now = datetime.datetime.now()
print(now)
s = now.strftime("%Y-%m-%d %H:%M:%S")
print(s)
#pthuc strptime(): chuyển chuỗi thành datetime:
from datetime import datetime
s1 = "2024-06-01 12:00:00"
dt1 = datetime.strptime(s1, "%Y-%m-%d %H:%M:%S")
print(dt1)
s2 = dt1.strftime("%d/%m/%Y %H:%M:%S")
print(s2)


