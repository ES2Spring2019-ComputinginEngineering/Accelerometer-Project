# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 17:59:10 2019

@author: Andrew
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as sig

time = np.arange(1,15,0.1) # create array with start, stop, and step size (similar concept to indices for list slicing)
y = np.cos(time)

# don't worry too much about this, but I'm adding random noise to the sine wave
noise = 0.3 * (np.random.rand(time.size) - 0.5)
y_noisy = y + noise



# Apply median filter to both original and noisy wave
y_filt = sig.medfilt(y)
y_noisy_filt = sig.medfilt(y_noisy)

# Find peaks of all waves
y_pks, _ = sig.find_peaks(y)
y_noisy_pks, _ = sig.find_peaks(y_noisy)
y_filt_pks, _ = sig.find_peaks(y_filt)
y_noisy_filt_pks, _ = sig.find_peaks(y_noisy_filt)


# Plot waveforms and their peaks
plt.subplot(2,2,1)
plt.plot(time, y, 'r-', time[y_pks], y[y_pks], 'b.')
plt.title('Original')
plt.subplot(2,2,2)
plt.plot(time, y_noisy, 'r-', time[y_noisy_pks], y_noisy[y_noisy_pks], 'b.')
plt.title('Noisy')

plt.subplot(2,2,3)
plt.plot(time, y_filt, 'r-', time[y_filt_pks], y_filt[y_filt_pks], 'b.')
plt.title('Original Median Filtered')
plt.subplot(2,2,4)
plt.plot(time, y_noisy_filt,'r-', time[y_noisy_filt_pks], y_noisy_filt[y_noisy_filt_pks], 'b.')
plt.title('Noisy Median Filtered')
plt.show()