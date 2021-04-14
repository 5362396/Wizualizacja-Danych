import matplotlib.pyplot as plt

x = [x for x in range(-100,101)]
y = [2*x+2 for x in range(-100,101)]
plt.plot(x, y, label='f(x) = 2x+2')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()

plt.show()