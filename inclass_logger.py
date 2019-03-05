from microbit import *
import random

print("Program Started")
display.show(Image.HAPPY) # Smiley Face displays when program starts correctly
filename = 'demo_data_' + str(random.randint(1,999)) + '.csv' # random filename to reduce overwriting

while not button_a.is_pressed(): #wait for button A to be pressed to begin logging
    sleep(10)

with open(filename, 'w') as outfile: # open text file to write to

    sleep(1000)
    display.show(Image.HEART) #Display Heart while logging

    t0 = running_time()

    #Read and store accelerometer data repeatedly until button A is pressed again
    while not button_a.is_pressed():
        t_elapse = running_time() - t0;
        light = display.read_light_level()
        b_pressed = button_b.is_pressed()
        comp_x = compass.get_x()
        combo_string = str(t_elapse) + "," + str(light) + "," + str(b_pressed) + "," + str(comp_x) + "\n"
        outfile.write(combo_string)

    display.show(Image.SQUARE) # Display Square when program ends

outfile.close()