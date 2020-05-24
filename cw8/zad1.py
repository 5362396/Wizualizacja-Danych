# Wczytaj do DataFrame arkusz z narodzinami dzieci w Polsce dostępny pod adresem https://dane.gov.pl/dataset/219.
import numpy as np
import pandas as pd
import xlrd
import openpyxl

plik = pd.ExcelFile('imiona.xlsx')
odczyt = pd.read_excel(plik, 'Arkusz1')
print(odczyt.sample())