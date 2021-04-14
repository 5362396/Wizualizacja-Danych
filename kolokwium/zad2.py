import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 6.1, 0.1)
f1 = np.cos(x)
f2 = np.cos(x+0.2)
f3 = np.cos(x+0.4)
f4 = np.cos(x+0.6)
plt.plot(x, f1, label='f(x) = cos(x)')
plt.plot(x, f2, label='f(x) = cos(x+0.2)', ls='--')
plt.plot(x, f3, label='f(x) = cos(x+0.4)', linewidth=3.0)
plt.plot(x, f4, label='f(x) = cos(x+0.6)', ls='-.')
plt.legend(loc=4)
plt.show()