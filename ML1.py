import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

x=np.random.normal(1.0,30.0,9)
y=np.random.normal(1.0,25.0,9)

 
# linear regression
slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))
"""

mymodel = np.poly1d(np.polyfit(x, y, 3))

myline = np.linspace(1, 22, 100)
"""

a=int(input("x:"))
s=myfunc(a)

plt.scatter(x, y)
plt.plot(x, mymodel,'r')
print(s)
plt.show()