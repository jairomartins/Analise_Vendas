# Importando as bibliotecas necessárias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Carrega o arquivo CSV
data_frame = pd.read_csv('datasets/sales_data.csv')

#visualizando os dados

# Exibe um gráfico de barras com a quantidade de vendas por região
# Colorindo as barras de acordo com a regiao 
data_frame['Region'].value_counts().plot(kind='bar', color=['blue', 'green', 'red', 'purple']) 
plt.xlabel('Região')# Nomeia o eixo x
plt.ylabel('Quantidade de vendas')# Nomeia o eixo y
plt.title('Vendas por região')# Adiciona um título ao gráfico
plt.show()# Exibe o gráfico


# Exibe um gráfico de barras com a quantidade de vendas por categoria de produto

# data_frame['Product_Category'].value_counts().plot(kind='bar', color=['blue', 'green', 'red', 'purple'])
# plt.xlabel('Categoria de produto')
# plt.ylabel('Quantidade de vendas')
# plt.title('Vendas por categoria de produto')
# plt.show()

#usando groupby para agrupar dados

# Agrupa os dados por região e calcula a média de vendas por região
# data_frame.groupby('Region')['Sales_Amount'].mean().plot(kind='bar', color=['blue', 'green', 'red', 'purple'])
# plt.xlabel('Região')
# plt.ylabel('Média de vendas')
# plt.title('Média de vendas por região')

# 
#print(data_frame.groupby('Region')['Sales_Amount'].mean())

# distribuicao por valor de venda 
# plt.figure(figsize=(10,8))
# data_frame['Sales_Amount'].plot(kind='hist', bins=30, color='blue', edgecolor='black')

# plt.xlabel('Valor da venda')
# plt.ylabel('Quantidade de vendas')
# plt.title('Distribuição de vendas por valor')
# plt.show()
