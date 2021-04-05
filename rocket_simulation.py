import math
import os
from random import *
from tkinter import *
import time
size = 600
root = Tk()
canvas = Canvas(root, width=size, height=size)
canvas.pack()

s_angle = int(input())
r_mass = int(input())
f_mass = int(input())
f_speed = int(input())
b_speed = int(input())
e_mass = int(input())
e_mass = 6 * (10 ** 24)
d_t = 0.03
x = 0
y = 0
G = 6.67 * (10 ** (-11))
r_earth = 6371000
r_speed = 0
it = 0
s_f = 600
tm = time.perf_counter()
while f_mass > 0:
    f_mass -= b_speed * d_t
    g = (G * e_mass) / ((r_earth + (x ** 2 + y ** 2) ** 0.5) ** 2)
    acceleration = (f_speed * b_speed) / (f_mass + r_mass)
    r_speed += (acceleration - g) * d_t
    x_speed = r_speed * math.cos(3.14 / (180 / s_angle));
    y_speed = r_speed * math.sin(3.14 / (180 / s_angle));
    x += x_speed * d_t
    y += y_speed * d_t
    if(time.perf_counter() - tm >= 1):
        print("coord= ",x, y)
        print("speed_x= ", x_speed , "speed_y= ", y_speed);
        print("mod speed = ", r_speed)
        print("fuel mass = ", f_mass)
        print()
        print()
        tm= time.perf_counter()
    canvas.create_oval(s_f - x / 40,s_f - y / 40,s_f - x / 40,s_f  - y / 40, fill='green')
    root.update()