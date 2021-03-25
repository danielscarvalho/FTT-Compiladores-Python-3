import matplotlib.pyplot as plt
from scipy import stats

# https://www.w3schools.com/python/python_ml_linear_regression.asp
# https://medium.com/@cs.sabaribalaji/overfitting-6c1cd9af589
# https://scikit-learn.org/0.15/auto_examples/plot_underfitting_overfitting.html
# https://medium.com/@brandyli1103/note-ml-solving-overfitting-on-linear-logistic-regression-2155ac11bad9

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()