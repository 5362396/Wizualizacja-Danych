def zamiana(krotka):
  lista=[]
  for i in range(6):
    lista.append(int(krotka[i],2))
  return lista

krotka=('101', '110', '1110', '111', '1101', '1001')
print(zamiana(krotka))