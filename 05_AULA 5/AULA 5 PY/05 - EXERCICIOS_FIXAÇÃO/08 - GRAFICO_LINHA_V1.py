#Exemp:https://matplotlib.org/stable/plot_types/basic/plot.html
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

# make data
x = np.linspace(0, 10, 100)
y = np.sin(x)
y1 = np.cos(x**2)

# plot
fig, ax = plt.subplots()

ax.plot(x, y,y1, linewidth=2.0)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()
