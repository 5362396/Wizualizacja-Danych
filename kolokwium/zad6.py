import pandas as pd
import matplotlib.pyplot as plt

plik = pd.ExcelFile('Najpopularniejsze-imiona-w-Polsce-w-latach-2000-2017.xlsx')
dane = pd.read_excel(plik)

popularne = dane.sort_values(by=['Liczba'],ascending=False)
print(popularne.head(5))