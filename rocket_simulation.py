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
e_mass = 6 * (10 ** 24)
d_t = 1
x = 0
y = 0
G = 6.67 * (10 ** (-11))
r_earth = 6371000
r_speed = 0
it = 0
s_f = 600
acceleration = 0
tm = time.perf_counter()
x_speed = 0
y_speed = 0
l = 9000
while y > 0 or f_mass > 0:
    if(f_mass > 0):
      f_mass -= b_speed * d_t
    g = (G * e_mass) / ((r_earth + (x ** 2 + y ** 2) ** 0.5) ** 2)
    if(f_mass > 0):
        acceleration = (f_speed * b_speed * d_t) / (f_mass + r_mass)
    else:
        acceleration = 0
    print("accel = ", acceleration)
    #r_speed += (acceleration) * d_t
    
    if not(acceleration != 0 and (acceleration * math.sin(3.14 / (180 / s_angle)) - g) * d_t < 0):
        x_speed += (acceleration * math.cos(3.14 / (180 / s_angle))) * d_t;
        y_speed += (acceleration * math.sin(3.14 / (180 / s_angle)) - g) * d_t;
    x += x_speed * d_t
    y += y_speed * d_t
    # if time.perf_counter() - tm >= 1:
    print("coord= ",x, y)
    print("speed_x= ", x_speed , "speed_y= ", y_speed);
    print("mod speed = ", r_speed)
    print("fuel mass = ", f_mass)
    print()
    print()
    tm = time.perf_counter()
    canvas.create_oval(s_f - x / l,s_f - y / l,s_f - x /l,s_f  - y / l, fill='green')
    root.update()

#45
#4000
#150000
#2500
#650
