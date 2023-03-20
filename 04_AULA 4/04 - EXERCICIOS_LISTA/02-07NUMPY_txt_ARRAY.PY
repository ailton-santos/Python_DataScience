import numpy as np

#SALVANDO UMA ARRAY

x = np.random.rand(10,10)

np.save('file.npy',x)

y = np.load('file.npy')

print(f"Segue matriz solicitada:{y}")
