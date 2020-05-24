# Zaimportuj pakiet itertools i znajdź w jego dokumentacji sposób na wygenerowanie kombinacji 3 elementowych bez powtórzeń na zbiorze 10 elementowym.
import itertools
liczby = {1,2,3,4,5,6,7,8,9,10}
wyniki=itertools.combinations(liczby,3)
while(True):
    print(next(wyniki))