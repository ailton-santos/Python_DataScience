#https://seaborn.pydata.org/examples/index.html#
import matplotlib.pyplot as plt
import seaborn as sns

#dados
data = [15,25,35,45]
labels = ['pardos','brancos','negros','asiaticos']


#paletas de cores
colors = sns.color_palette("tab10")
#colors = sns.color_palette('pastel')[0:5]

#cria o grafico

plt.pie(data, labels = labels, colors=colors, autopct='%.0f%%')
plt.show()


#realizar o mesmo processo com outros exemplos