import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 6, 0.1)
f1 = np.cos(x)
f2 = np.sin(x)
f3 = -f1
f4 = -f2
plt.plot(x, f1, label='f(x) = cos(x)')
plt.plot(x, f2, label='f(x) = sin(x)', ls='--')
plt.plot(x, f3, label='f(x) = -cos(x)', linewidth=3.0)
plt.plot(x, f4, label='f(x) = -sin(x)', ls='-.')
plt.legend(loc=4)
plt.show()