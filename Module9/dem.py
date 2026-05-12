def dem(tong):
    dem = 0
    for c in str(tong):
        if int(c) % 2 == 0:
            dem += 1
    return dem