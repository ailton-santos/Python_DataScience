import numpy as np

csv_array = np.random.rand(10,10)

np.savetxt('csv_array.csv',csv_array)

x= np.loadtxt('csv_array.csv')

print(x)