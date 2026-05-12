from dem import *
from Tim import *
from Tinh import *

x =int(input("X= "))
y = int(input("Y= "))
z = int(input("Z = "))
tich_so = tinhTich(x,y,z)
dem = dem(tich_so)
max = Timmax(tich_so)
print(max)
print(dem)
print(tich_so)
