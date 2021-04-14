import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('studenci.csv', sep=';', header=0)

tryb1 = df[df['Tryby nauczania'] == 'studia stacjonarne (dzienne)']
tryb1_sorted = tryb1.sort_values(by='Rok')
tryb1_sorted_woman = tryb1_sorted[tryb1_sorted['Płeć'] == "kobiety"]
tryb1_sorted_man = tryb1_sorted[tryb1_sorted['Płeć'] == "mężczyźni"]

tryb2 = df[df['Tryby nauczania'] == 'studia niestacjonarne']
tryb2_sorted = tryb2.sort_values(by='Rok')
tryb2_sorted_woman = tryb2_sorted[tryb2_sorted['Płeć'] == "kobiety"]
tryb2_sorted_man = tryb2_sorted[tryb2_sorted['Płeć'] == "mężczyźni"]

plt.subplot(3, 1, 1)
plt.xticks([2016, 2017])
plt.title('studia stacjonarne (dzienne)')
plt.plot(tryb1_sorted_woman['Rok'], tryb1_sorted_woman['Wartosc'], label="Kobiety")
plt.plot(tryb1_sorted_man['Rok'], tryb1_sorted_man['Wartosc'], label="Mężczyźni")

plt.subplot(3, 1, 2)
plt.xticks([2016, 2017])
plt.title('studia niestacjonarne')
plt.plot(tryb2_sorted_woman['Rok'], tryb2_sorted_woman['Wartosc'], label="Kobiety")
plt.plot(tryb2_sorted_man['Rok'], tryb2_sorted_man['Wartosc'], label="Mężczyźni")

plt.legend()
plt.show()