import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('kina.csv', sep=';' )

rok2015 = df[df["Rok"]==2015]
df1 = pd.DataFrame(rok2015)
rok2016 = df[df["Rok"]==2016]
df2 = pd.DataFrame(rok2016)
rok2017 = df[df["Rok"]==2017]
df3 = pd.DataFrame(rok2017)
print(df3)

gestor1 = df[df["Gestor"]=="własność gminy / miasta na prawach powiatu"]
gestor1 = gestor1.sort_values(by='Rok')

gestor2 = df[df["Gestor"]=="własność powiatu"]
gestor2 = gestor2.sort_values(by='Rok')

gestor3 = df[df["Gestor"]=="własność województwa"]
gestor3 = gestor3.sort_values(by='Rok')

plt.subplot(3, 1, 1)
plt.xticks([2015,2016,2017])
plt.plot(gestor1['Rok'], gestor1['Wartosc'])
plt.subplot(3, 1, 2)
plt.xticks([2015,2016,2017])
plt.plot(gestor2['Rok'], gestor2['Wartosc'])
plt.subplot(3, 1, 3)
plt.xticks([2015,2016,2017])
plt.plot(gestor3['Rok'], gestor3['Wartosc'])

plt.show()