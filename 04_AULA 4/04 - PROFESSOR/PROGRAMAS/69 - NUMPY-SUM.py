import numpy as np

minha_lista_1=[[30, 60, 270],[1,2,3]]

# soma os valores de array ao longo de um eixo
x = np.sum(minha_lista_1,axis=0)

print(x)