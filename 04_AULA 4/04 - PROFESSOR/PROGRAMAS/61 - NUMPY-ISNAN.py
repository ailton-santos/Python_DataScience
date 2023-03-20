import numpy as np

minha_lista=[-1.7, np.nan , -0.2, 0.2, 1.5, 1.7, 2.0]

# retorna um array booleano indicando se cada elemento é vazio (Not a Number)
x = np.isnan(minha_lista)

print(x)