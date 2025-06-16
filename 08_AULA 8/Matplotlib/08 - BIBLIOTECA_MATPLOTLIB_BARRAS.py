import matplotlib.pyplot as plt
import numpy as np

#dados
labels = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai','Jun','Jul','Ago','Set','Out','Nov','Dez']
men_means = [20, 34, 30, 35, 27,24,23,40,32,21,27,36]
women_means = [25, 32, 34, 20, 25, 20, 36, 50, 23, 42,24,22]
#eixo X
x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars
#Unindo dados no mesmo eixo criando rotulo de dados
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, men_means, width, label='Homens')
rects2 = ax.bar(x + width/2, women_means, width, label='Mulheres')

# Adicione alguns textos para rótulos, 
# rótulos de marcação de título e eixo x personalizado, etc.
ax.set_ylabel('Scores')
ax.set_title('Quantidade de visitas na loja X genero')
ax.set_xticks(x, labels)
ax.legend()
ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)
fig.tight_layout()
plt.show()