import pandas as pd
import matplotlib.pyplot  as plt

# Criando sua base de dados
df = pd.DataFrame({'Turismo': ['Italia', 'India', 'Mexico', 'China'],
                   'Rendimentos em millhoes': [20, 27, 15, 36]})
  
# impressão do grafico de barra horizontal veja: barh
df.plot.barh(x='Turismo', y='Rendimentos em millhoes',
             title='Ranking de Turismo', color='orange')

plt.show()
