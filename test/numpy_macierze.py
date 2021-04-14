import numpy as np
#a
m1 = np.random.randint(1, 11, (5, 5))
m2 = np.random.randint(1, 11, (5, 5))
print(m1)
print("\n")
print(m2)
print("\n")
#b
m1 *=2
m2 *=2
print(m1)
print("\n")
print(m2)
print("\n")
#c
pionowa = np.concatenate((m1,m2))
print(pionowa)
print("\n")
#d
kol2 = pionowa[:,1]
kol3 = pionowa[:,2]
print(np.hstack([kol2,kol3]))