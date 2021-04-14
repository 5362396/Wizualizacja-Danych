import numpy as np
import matplotlib.pyplot as plt

x=np.arange(-10,10,0.5)
niebieski=pow(x,2)+(2*x)-4
zielony=(2*np.cos(x+5))
pomaranczowy=-pow(x,3)+x-2
plt.grid(True)
plt.plot(x,niebieski,"b.",label="niebieski")
plt.plot(x,zielony,"g--",label="zielony")
plt.plot(x,pomaranczowy,"-.",color="orange",label="pomaranczowy")
plt.legend()
plt.xlabel('oś pozioma')
plt.ylabel('oś pionowa po lewej stronie')
plt.title("Parę wykresów")
plt.show()