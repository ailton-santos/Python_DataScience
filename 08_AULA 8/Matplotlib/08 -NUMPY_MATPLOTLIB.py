import numpy as np
import matplotlib.pyplot as plt

#exemplo para um grafico de linha

a = np.random.rand(10)

plt.plot(a)
plt.show()
#plt.savefig('Figure_1.png')

#############################################

# exemplo para um grafico com pontos
#uso do linspace cria pontos dentro de um intervalo determinado.

x = np.linspace(2.0, 3.0,30) 
y = np.linspace(0, 10, 30)
plt.plot(x, y, 'red') # line
plt.plot(x, y, 'o')# dots
plt.show()
#plt.savefig('Figure_2.png')
#########################################

#exemplo grafico 3d

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
X = np.arange(-1, 1, 0.1)
Y = np.arange(-1, 1, 0.1)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis')

plt.show()
#plt.savefig('Figure_3.png')