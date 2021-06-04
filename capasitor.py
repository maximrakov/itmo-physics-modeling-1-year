import math
import matplotlib.pyplot as plt
import os
import sys

q = 1.6 * (10 ** (-19))
m = 9.11 * (10 ** (-31))
mv = 0

u = int(input()) #Напряжение между обкладками.
r2 = float(input()) #Радиус внешнего цилиндра
d = float(input()) #расстояние между обкладками
l = float(input()) #Длина конденсатора.
eps = float(input()) #Диэлектрическая проницаемость материала конденсатора.
vx = int(input()) #Скорость электрона в момент в начальный момент.
vy = 0
r1 = r2 - d 
pos = (r1 + r2) / 2
x = 0
y = pos - r1
ay = 0
it = 10 ** (-9)
tm = 0

cord_x = []
cord_y = []
tma = []
va = []
aa = []

while x < l:
	tm += 1
	a = (q * u) / (pos * math.log(r2 / (r2 - d)))
	a /= m
	vy += a * it
	y += vy * it
	x += vx * it
	pos += vy * it
	mv = (vx ** 2 + vy ** 2) ** 0.5

	cord_x.append(x)
	cord_y.append(y)
	tma.append(it * tm)
	va.append(mv)
	aa.append(a);
	os.system('cls')
	print("time= ",tm * it)
	print("x = ", x)
	print("y = ", y)
	print("v= ", mv)
	print("a= ", a)
	print("vy = ", vy)

	print()
	print()

plt.plot(cord_x, cord_y)
plt.xlabel("x")
plt.ylabel("y")
plt.show()

plt.plot(tma, cord_y)
plt.xlabel("time")
plt.ylabel("y")
plt.show()

plt.plot(tma, va)
plt.xlabel("time")
plt.ylabel("speed")
plt.show()

plt.plot(tma, aa)
plt.xlabel("time")
plt.ylabel("acceleration")
plt.show()