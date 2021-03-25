import matplotlib.pyplot as plt
import numpy as np

# https://www.w3schools.com/python/matplotlib_histograms.asp

x = np.random.normal(170, 10, 250)
#x = [1,5,10,4,0]

plt.hist(x)
plt.show() 