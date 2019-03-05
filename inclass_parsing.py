# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 10:28:29 2019

@author: Andrew
"""

import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt

filename = "demo_data_931.csv"
#t_start = 2000
#t_end = 5000

t_temp = [];
light_temp = [];
button_temp = [];
compx_temp = [];

fin = open(filename, 'r')

for line in fin:
    split_line = line.split(",")
    #if int(split_line[0]) > t_start and int(split_line[0]) < t_end:
    t_temp.append(int(split_line[0]))
    light_temp.append(int(split_line[1]))
    button_temp.append((split_line[2]) == "True")
    compx_temp.append(int(split_line[3]))

fin.close() 

t_ms = np.array(t_temp)
light = np.array(light_temp)
button = np.array(button_temp)
comp_x = np.array(compx_temp)

t_s = t_ms /1000

plt.figure(1)
plt.plot(t_s, light)
plt.title('Light vs Time')
plt.xlabel('Time (s)')
plt.ylabel('Brightness (0-255)')

plt.figure(2)
plt.plot(t_s, button)
plt.title('Button Status vs Time')
plt.xlabel('Time (s)')
plt.ylabel('Pressed?')

plt.figure(3)
plt.plot(t_s, comp_x)
plt.title('Compass x-values vs Time')
plt.xlabel('Time (s)')
plt.ylabel('?')


