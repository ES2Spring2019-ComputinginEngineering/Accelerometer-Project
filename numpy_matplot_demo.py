import matplotlib.pyplot as plt
import numpy as np

# regular python lists
x_list = [1, 2, 3, 4, 5]
y_list = [1, 4, 9, 16, 25]

print('Indexing in Python List:', x_list[1])

# convert to numpy arrays
x_numpy = np.array(x_list)
y_numpy = np.array(y_list)


print('Indexing in Numpy Array:', x_numpy[1])

# Adding Python Lists
z_list = []
for i in range(0, len(x_list)):
  z_list.append(x_list[i] + y_list[i])

print('Adding in Python List:', z_list)

# Adding Numpy Arrays
z_numpy = x_numpy + y_numpy
# Multiplication
y2_numpy = 2 * x_numpy

print('Adding in Numpy Array:', z_numpy)

plt.figure(1)
plt.plot(x_numpy, y_numpy, 'ro--', x_numpy, y2_numpy, 'kd-.')
#Y is red dashed line with circles
#Y2 is black dot-dash line with diamonds
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Y vs X')
plt.legend(('Y', 'Y2'))
plt.xlim((-1, 8)) # set x range to -1 to 8
plt.grid()
plt.show()