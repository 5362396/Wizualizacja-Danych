import pandas as pd
import matplotlib.pyplot as plt

a = pd.read_csv('kghm_od_2000.csv', delimiter=',')
print(a.loc[((a.Data >= '2010.01.01') & (a.Data < '2011.01.01')), ['Wolumen']].sum())
a['Rok'] = pd.DatetimeIndex(a['Data']).year

grupa = a.groupby(['Rok']).agg({'Wolumen': ['sum']})
grupa.plot.bar()
plt.xticks(rotation=45)
plt.ylabel('Ilość Wolumenu')
plt.xlabel('Rok')
plt.show()