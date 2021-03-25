#pip install matplotlib
#pip install numpy

import matplotlib.pyplot as plt
import numpy as np

#https://www.w3schools.com/python/matplotlib_scatter.asp

gsize=10

x = np.random.randint(100, size=(gsize))
y = np.random.randint(100, size=(gsize))

colors = np.random.randint(100, size=(gsize))
#sizes = 10 * np.random.randint(100, size=(100))
sizes = 100 * np.arange(gsize)


plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')

plt.colorbar()

plt.show()