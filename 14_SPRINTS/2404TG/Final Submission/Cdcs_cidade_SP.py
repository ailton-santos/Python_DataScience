#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[77]:


dados = pd.read_csv('equipamentos-administracao-indireta---cdcs.csv', ';', encoding = 'iso-8859-1' )


# In[80]:


df = pd.DataFrame(dados)
df


# In[83]:


dados.head()


# In[85]:


df_sem_duplicatas = df.drop_duplicates()
df_sem_duplicatas


# In[86]:


df_sem_na = df.dropna()  
df_sem_na = df.dropna(axis=1)  
df_sem_na


# In[149]:


sns.catplot(data=dados, x="ZONA", y="PREFEITURA REGIONAL", hue="ZONA")


# In[174]:


resultado_df = dados[['PREFEITURA REGIONAL','ZONA']]
display(resultado_df)


# In[175]:


df_zona = resultado_df.groupby('PREFEITURA REGIONAL')['ZONA'].count().reset_index()
df_zona


# In[183]:


janela = plt.figure(figsize=(25,10))
grafico = janela.add_axes([0,0,1,1])
grafico.bar(df_zona['PREFEITURA REGIONAL'], df_zona['ZONA'])
plt.xticks(rotation=45)
plt.ylabel('NOME')
plt.xlabel('PREFEITURA REGIONAL')
plt.title('Grafico por Prefeitura Regional')
plt.show()

