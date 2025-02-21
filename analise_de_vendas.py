import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Carrega o arquivo CSV
data_frame = pd.read_csv('datasets/sales_data.csv')

# Exibe as 5 primeiras linhas do data_frame
data_frame.head()

#print(data_frame.head())

# Product_ID   Sale_Date Sales_Rep Region  Sales_Amount  Quantity_Sold Product_Category  Unit_Cost  Unit_Price Customer_Type  Discount Payment_Method Sales_Channel Region_and_Sales_Rep
# 0        1052  2023-02-03       Bob  North       5053.97             18        Furniture     152.75      267.22     Returning      0.09           Cash        Online            North-Bob
# 1        1093  2023-04-21       Bob   West       4384.02             17        Furniture    3816.39     4209.44     Returning      0.11           Cash        Retail             West-Bob
# 2        1015  2023-09-21     David  South       4631.23             30             Food     261.56      371.40     Returning      0.20  Bank Transfer        Retail          South-David
# 3        1072  2023-08-24       Bob  South       2167.94             39         Clothing    4330.03     4467.75           New      0.02    Credit Card        Retail            South-Bob
# 4        1061  2023-03-24   Charlie   East       3750.20             13      Electronics     637.37      692.71           New      0.08    Credit Card        Online         East-Charlie

data_frame.info()  # Mostra informações sobre o data_frame


print(data_frame.describe()) # Exibe informações estatísticas sobre o data_frame

# Exibe a quantidade de valores nulos em cada coluna
print(data_frame.isnull().sum()) 

# Exibe se contem dados duplicados no data_frame
data_frame.duplicated().sum()
print(data_frame.duplicated().sum()) 

#visualizando os dados

# Exibe um gráfico de barras com a quantidade de vendas por região
# Colorindo as barras de acordo com a regiao 
data_frame['Region'].value_counts().plot(kind='bar', color=['blue', 'green', 'red', 'purple'])
plt.xlabel('Região')
plt.ylabel('Quantidade de vendas')
plt.title('Vendas por região')
# plt.show()


# Exibe um gráfico de barras com a quantidade de vendas por categoria de produto

data_frame['Product_Category'].value_counts().plot(kind='bar', color=['blue', 'green', 'red', 'purple'])
plt.xlabel('Categoria de produto')
plt.ylabel('Quantidade de vendas')
plt.title('Vendas por categoria de produto')
# plt.show()

#usando groupby para agrupar dados

# Agrupa os dados por região e calcula a média de vendas por região
data_frame.groupby('Region')['Sales_Amount'].mean().plot(kind='bar', color=['blue', 'green', 'red', 'purple'])
plt.xlabel('Região')
plt.ylabel('Média de vendas')
plt.title('Média de vendas por região')

# 
print(data_frame.groupby('Region')['Sales_Amount'].mean())

# distribuicao por sales_amount
plt.figure(figsize=(10,8))
data_frame['Sales_Amount'].plot(kind='hist', bins=30, color='blue', edgecolor='black')

plt.xlabel('Valor da venda')
plt.ylabel('Quantidade de vendas')
plt.title('Distribuição de vendas por valor')
plt.show()
