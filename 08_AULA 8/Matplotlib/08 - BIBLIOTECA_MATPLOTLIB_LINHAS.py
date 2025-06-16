import matplotlib.pyplot as plt
import numpy as np

# dados para impressão
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(4 * np.pi * t)

fig, ax = plt.subplots()
ax.plot(t, s)
ax.set(xlabel='Tempo (s)', ylabel='Tensão (mV)',
       title='Variação da tensão X tempo')
ax.grid()

#fig.savefig("test.png")
plt.show()

