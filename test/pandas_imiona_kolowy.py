import pandas as pd
import matplotlib.pyplot as plt

plik = pd.ExcelFile('Najpopularniejsze-imiona-w-Polsce-w-latach-2000-2017.xlsx')
dane = pd.read_excel(plik)
#print(dane)

dane10 = dane[dane['Rok'] == 2010]
popularne = dane10.sort_values(by=['Liczba'],ascending=False)
print(popularne.head(3))

grupa = dane.groupby(['Plec']).agg({'Liczba':['sum']})
grupa.plot.pie(subplots = True,autopct='%.2f %%')
plt.show()