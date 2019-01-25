from microbit import *

print("Program Started")
display.show(Image.HAPPY)

with open('acc.txt', 'w') as outfile:

    #while not button_a.is_pressed():
    #    sleep(10)

    display.show(Image.HEART)
    sleep(1000)

    while not button_a.is_pressed():
        print("Logging")
        accx = accelerometer.get_x()
        accy = accelerometer.get_y()
        accz = accelerometer.get_z()
        acc_string = str(accx) + ", " + str(accy) + ", " + str(accz) + "\n"
        outfile.write(acc_string)
