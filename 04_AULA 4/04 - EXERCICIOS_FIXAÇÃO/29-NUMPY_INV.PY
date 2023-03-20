
import numpy as np

lista1 = np.array( [[5,3],[3,5] ])


#determinante da matriz
x = np.linalg.inv(lista1)
id = np.multiply(lista1,x)
  

print(x)
print(id)