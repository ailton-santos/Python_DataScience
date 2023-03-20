import numpy as np

minha_lista=[-1.7, -1.5, -0.2, 0.2, 1.5, 1.7, 2.0]

# arredonda os elementos para inteiro mais próximo, preservando o dtype
x = np.rint(minha_lista)

print(x)