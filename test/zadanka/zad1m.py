import numpy as np
import matplotlib.pyplot as plt

wysokosci1 = [30, -10, -20, -50, -70]
wysokosci2 = [-30, -10, -20, -50, -70]
wysokosci3 = [-30, -10, -20, -50, -70]
wysokosci4 = [-30, -10, -20, -50, -70]
wysokosci5 = [-30, -10, -20, -50, -70]
wysokosci6 = [-30, -10, -20, -50, -70]
etykiety1 = ('A', 'B', 'C', 'D', 'E')
x = np.arange(len(wysokosci1))
plt.barh(x, wysokosci1)
plt.barh(x, wysokosci2)
plt.barh(x, wysokosci2)
plt.barh(x, wysokosci4)
plt.barh(x, wysokosci5)
plt.barh(x, wysokosci6)

plt.yticks(x, etykiety1)
plt.title('Tytul1')
plt.show()