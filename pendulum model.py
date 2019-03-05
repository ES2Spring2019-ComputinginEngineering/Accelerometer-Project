#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 13:13:45 2019

@author: jenncross
"""

import matplotlib.pyplot as plt
import numpy as np
import math

g = -9.8 #meters per second per second
l = .5 #meter

def update_system(acc,pos,vel,time1,time2):
    # position and velocity update below
    dt = time2-time1
    posNext = pos+vel*dt
    velNext = vel+acc*dt
    accNext = g/l*math.cos((math.pi/2)-pos)
    return posNext,velNext,accNext

def print_system(time,pos,vel):
    print("TIME:     ", time)
    print("POSITION: ", pos)
    print("VELOCITY: ", vel, "\n")

def sim(t_step):
    # initial conditions
    pos = [math.pi/4]
    vel = [0]
    acc = [0]
    time = np.linspace(0,10,t_step)
    #print_system(time[0],pos[0],vel[0])
    
    i = 1
    while i < len(time):
        # update position and velocity using previous values and time step
        posNext, velNext, accNext = update_system(acc[i-1],pos[i-1],vel[i-1],time[i-1],time[i])
        pos.append(posNext)
        vel.append(velNext)
        acc.append(accNext)
        #print_system(time[i],pos[i],vel[i])
        i += 1
    
    plt.figure(figsize=(4,6))
    plt.subplot(3,1,1)
    plt.plot(time, pos, 'r-') 
    
    plt.xlabel('Time (seconds)')
    plt.ylabel('Position (m)')
    plt.title('Position vs Time')
    #plt.xlim((0, 10)) # set x range to -1 to 8
    plt.grid()
    
    
    plt.subplot(3,1,2)
    plt.plot(time, vel, 'b-') 
    plt.xlabel('Time (seconds)')
    plt.ylabel('Velocity (m/s)')
    plt.title('Velocity vs Time')
    plt.xlim((0, 10)) # set x range to -1 to 8
    plt.grid()
    
    
    plt.subplot(3,1,3)
    plt.plot(time, acc, 'k-') 
    plt.xlabel('Time (seconds)')
    plt.ylabel('Acceleration (m/s^2)')
    plt.title('Acceleration vs Time')
    plt.xlim((0, 10)) # set x range to -1 to 8
    plt.grid()
    plt.tight_layout()
    plt.show()
    
for i in [1, 10, 100, 1000, 10000, 100000]:
    sim(i)