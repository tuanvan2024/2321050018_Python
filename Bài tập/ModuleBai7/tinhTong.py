from KiemTra import KiemTra
def tinhTong(x):
    tong = 0
    for v in x:
        if KiemTra(v):   # gọi module 2
            tong += v
    return tong