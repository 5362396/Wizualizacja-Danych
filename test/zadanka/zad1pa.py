import numpy as np
import matplotlib.pyplot as plt

x=np.arange(-4,4,0.1)
f1 = -pow(x, 3)+(3*x)-7
f2 = 3*(np.log(2*x) / np.log(4))
f3 = -4+3*x
plt.grid(True)
plt.plot(x, f1, label='f(x) = -x^3+3x-7')
plt.plot(x, f2, label='f(x) = 3*log4(2x)')
plt.plot(x, f3, label='f(x) = -4+3x')
plt.legend(loc=4)
plt.show()