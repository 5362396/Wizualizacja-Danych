import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

f = pd.ExcelFile('biblioteka.xlsx')
df = pd.read_excel(f)
pomocnicza = df[df['Biblioteki'] == 'księgozbiór']
suma1 = pomocnicza.groupby(['Rok']).agg({'Wartosc':['sum']})
pomocnicza2 = df[df['Biblioteki'] == 'czytelnicy w ciągu roku']
suma2 = pomocnicza2.groupby(['Rok']).agg({'Wartosc':['sum']})

print(suma1/suma2)


czytelnicy = df[df['Biblioteki'] == 'czytelnicy w ciągu roku']
ksiazki =  df[df['Biblioteki'] == 'księgozbiór']
x = np.arange(0, len(czytelnicy))
plt.bar(x-0.25,czytelnicy['Wartosc'],label="Czytelnicy", width=0.25, color="blue")
plt.bar(x,ksiazki['Wartosc'],label="Ksiazki", width=0.25, color="red")
plt.xticks(x, czytelnicy["Rok"])
plt.legend(loc = 9)
plt.title('Czytelnicy i Ksiażki na czytelnika')
plt.show()