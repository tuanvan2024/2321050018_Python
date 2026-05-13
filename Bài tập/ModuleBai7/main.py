from DieuKien import *
from Output import *
from Input import *
from tinhTong import *
def main():
    x        = nhap()
    tong     = tinhTong(x)
    ket_qua  = kiemtra1(tong)
    xuat(tong, ket_qua)

main()