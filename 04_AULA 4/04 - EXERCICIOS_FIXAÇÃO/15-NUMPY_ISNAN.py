
import numpy as np

lista = [454 , np.nan ,45 , 65, (0/1000000) ]
# Retorno um array boolean indica se cada elemnto é vazio
x = np.isnan(lista)  

print(x)