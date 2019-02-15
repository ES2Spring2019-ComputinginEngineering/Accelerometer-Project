from IPython import get_ipython
get_ipython().magic('reset -sf')

import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt

filename = "accelerometer_data_911.txt"
t_start = 2000
t_end = 5000

t_temp = [];
x_temp = [];
y_temp = [];
z_temp = [];

fin = open(filename, 'r')

for line in fin:
    split_line = line.split("\t")
    if int(split_line[0]) > t_start and int(split_line[0]) < t_end:
        t_temp.append(int(split_line[0]))
        x_temp.append(int(split_line[1]))
        y_temp.append(int(split_line[2]))
        z_temp.append(int(split_line[3]))

fin.close() 

t_ms = np.array(t_temp)
x_acc = np.array(x_temp)
y_acc = np.array(y_temp)
z_acc = np.array(z_temp)

t_s = t_ms /1000

tot_acc = np.sqrt(np.square(x_acc) + np.square(y_acc))
filt_acc = sig.medfilt(tot_acc)

reg_peaks, _ = sig.find_peaks(tot_acc)
filt_peaks, _ = sig.find_peaks(filt_acc)


period = np.empty(filt_peaks.size-1)
for i in range(0, filt_peaks.size-1):
    period[i] = (t_s[filt_peaks[i+1]] - t_s[filt_peaks[i]])




plt.figure(1)
plt.plot(t_s, x_acc, t_s, y_acc, t_s, z_acc)
plt.legend(('X','Y','Z'))

plt.figure(2)
plt.plot(t_s, tot_acc, t_s, filt_acc)
plt.plot(t_s[reg_peaks], tot_acc[reg_peaks], 'ro', t_s[filt_peaks], tot_acc[filt_peaks], 'bs')


plt.show()