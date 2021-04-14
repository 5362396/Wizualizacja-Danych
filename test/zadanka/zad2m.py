import pandas as pd
import matplotlib.pyplot as plt

plik = pd.ExcelFile('sport.xlsx')
dane = pd.read_excel(plik)

grupa = dane.groupby(['Gry zespołowe']).agg({'Wartosc': ['mean']})
print(grupa)

explode = (0, 0, 0, 0.1)
grupa.plot.pie(subplots=True, explode=explode, autopct='%.2f %%')
plt.title('Sporty - średnia ćwiczących')
plt.savefig('zad2.pdf')
plt.show()
