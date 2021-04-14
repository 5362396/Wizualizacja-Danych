import pandas as pd
import matplotlib.pyplot as plt

plik = pd.read_csv('kghm_od_2000.csv', delimiter=',')
print(plik.loc[((plik.Data >= '2003.01.01') & (plik.Data < '2006.01.01')), ['Wolumen']].max())
print(plik.loc[((plik.Data >= '2003.01.01') & (plik.Data < '2006.01.01')), ['Wolumen']].min())



plik['Rok'] = pd.DatetimeIndex(plik['Data']).year
plik['Miesiac'] = pd.DatetimeIndex(plik['Data']).month
data = plik[plik['Rok'] == 2010]
data2 = data.groupby(['Miesiac']).agg({'Zamkniecie':['mean']})
data2.plot()
plt.show()