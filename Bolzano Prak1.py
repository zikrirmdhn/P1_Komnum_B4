import matplotlib.pyplot as plt
import numpy as np

def func(n : float):
    return pow(10,n)+2*n-100

print("tebak dulu batas kiri dan kanan nya (left < right) : \n")
left = float(input('left : '))
right = float(input('right : '))

while (func(left)*func(right) > 0) :
    print("tebakanmu kurang jitu, masukkan tebakan baru\n")
    left = float(input('left : '))
    right = float(input('right : '))

count = 0
while (count<10) :
    print("Iterasi ke -", count+1)
    mid = left+((right-left)/2)
    print("F(", round(left, 4), ")\t: ", round(func(left), 4))
    print("F(", round(right, 4), ")\t: ", round(func(right), 4))
    print("F(", round(mid, 4), ")\t: ", round(func(mid), 4), "\n")

    if (func(mid)*func(left) < 0) : right = mid
    elif (func(mid)*func(right) < 0) : left = mid

    count = count+1

print("F(", round(left, 4), ")\t: ", round(func(left), 4))
print("F(", round(right, 4), ")\t: ", round(func(right), 4))

if ((0-func(left)) < (func(right))) : print("solution is x = ", round(left, 4))
else : print("solution is x = ", round(right, 4))

x = np.linspace(-10,10,num = 1000)
y = func(x)
plt.plot(x, y)
plt.show()
plt.xlabel('X')
plt.ylabel('Y')