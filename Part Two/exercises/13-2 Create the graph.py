## This is course material for Introduction to Python Scientific Programming
## Example code: matplotlib_basic_plot.py
## Author: Allen Y. Yang
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

import matplotlib.pyplot as plt
import numpy as np

# generate a basic sample point array on x-axis
#x = np.arange(1., 3.0, 0.1)

# Create a sin function sample
#y0 = np.
#plt.plot(x, x, color = 'r', linewidth = 3)
plt.plot([1, 2, 3], [2, 4, 1])
plt.ylabel('y-axis')
plt.xlabel('x-axis')
plt.title('Sample graph!')

# Create a dash cos function sample
#y1 = np.cos(x)
#plt.plot(x, y1, 'b--', linewidth = 1)
plt.ylim(1, 4)
plt.xlim(1.0,3.0)
plt.xticks(np.arange(1.0,3.1,step=0.5))
plt.show()