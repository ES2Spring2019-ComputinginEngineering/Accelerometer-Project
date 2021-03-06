from microbit import *
import random

print("Program Started")
display.show(Image.HAPPY) # Smiley Face displays when program starts correctly
filename = 'accelerometer_data_' + str(random.randint(1,999)) + '.txt' # random filename to reduce overwriting


while not button_a.is_pressed(): #wait for button A to be pressed to begin logging
    sleep(10)

with open(filename, 'w') as outfile: # open text file to write to

    sleep(1000)
    display.show(Image.HEART) #Display Heart while logging

    t0 = running_time()

    #Read and store accelerometer data repeatedly until button A is pressed again
    while not button_a.is_pressed():
        t_elapse = running_time() - t0;
        accx = accelerometer.get_x()
        accy = accelerometer.get_y()
        accz = accelerometer.get_z()
        acc_string = str(t_elapse) + "\t" + str(accx) + "\t" + str(accy) + "\t" + str(accz) + "\n"
        outfile.write(acc_string)

    display.show(Image.SQUARE) # Display Square when program ends

outfile.close()

# Instructions:
# Flash this program onto microbit
# Smiley Face should appear on screen
# Disconnect microbit from computer and attach to pendulum
# Press Button A to begin logging data
# After a 1 second delay the microbit will display a heart and begin logging
# Press Button A again to stop logging data
# A Square should appear on the screen
# Reconnect to computer and open Mu
# Click the 'Files' Button
# Drag 'accelerometer_data.txt' from 'Files on your micro:bit:' to 'Files on your computer:'
# Right click the filename and select 'Open'
# You should see the accelerometer data