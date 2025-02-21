# Análise de Dados - Estudo Básico

Este repositório é dedicado ao estudo básico de análise de dados. Aqui, você encontrará exemplos, scripts e anotações sobre conceitos fundamentais de análise de dados, utilizando ferramentas como Python, Pandas, Matplotlib, e outras bibliotecas populares.

## Objetivo

O objetivo deste repositório é guardar os códigos utilizados durante o estudo. Os tópicos abordados incluem manipulação de dados, visualização, estatísticas descritivas e muito mais.


## Estrutura do Projeto

📂 **Analise_Vendas**  
├── 📂 **datasets**  
│   ├── 📄 sales_data.csv  
├── 📄 analise_de_vendas.py  
├── 📄 README.md  

### Descrição dos Arquivos

- 📂 **datasets/**: Contém os arquivos de dados usados para a análise.  
  - 📄 `sales_data.csv`: Conjunto de dados de vendas.  
- 📄 **analise_de_vendas.py**: Script principal para análise dos dados.  
- 📄 **README.md**: Documentação do projeto. 


## Vamos começar ! 

Importando as bibliotecas necessárias:

```bash
pip install pandas matplotlib seaborn numpy

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```

Carregando o Arquivo CSV com os dados das vendas

```bash

data_frame = pd.read_csv('datasets/sales_data.csv')

```

## Visualizando a estrutura dos dados

Com o método .head() visualizamos as 5 primeiras linhas do DataFrame

```bash

>>> print(data_frame.head())

  Product_ID   Sale_Date Sales_Rep Region  Sales_Amount  Quantity_Sold Product_Category  Unit_Cost  Unit_Price Customer_Type  Discount Payment_Method Sales_Channel Region_and_Sales_Rep
0        1052  2023-02-03       Bob  North       5053.97             18        Furniture     152.75      267.22     Returning      0.09           Cash        Online            North-Bob
1        1093  2023-04-21       Bob   West       4384.02             17        Furniture    3816.39     4209.44     Returning      0.11           Cash        Retail             West-Bob
2        1015  2023-09-21     David  South       4631.23             30             Food     261.56      371.40     Returning      0.20  Bank Transfer        Retail          South-David
3        1072  2023-08-24       Bob  South       2167.94             39         Clothing    4330.03     4467.75           New      0.02    Credit Card        Retail            South-Bob
4        1061  2023-03-24   Charlie   East       3750.20             13      Electronics     637.37      692.71           New      0.08    Credit Card        Online         East-Charlie

```
Com o método .info() conseguimos imprimir informações sobre um DataFrame, incluindo o tipo de índice e colunas, valores não nulos e uso de memória.

``` bash
>>> print(data_frame.info())

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1000 entries, 0 to 999
Data columns (total 14 columns):
 #   Column                Non-Null Count  Dtype  
---  ------                --------------  -----  
 0   Product_ID            1000 non-null   int64  
 1   Sale_Date             1000 non-null   object 
 2   Sales_Rep             1000 non-null   object 
 3   Region                1000 non-null   object 
 4   Sales_Amount          1000 non-null   float64
 5   Quantity_Sold         1000 non-null   int64  
 6   Product_Category      1000 non-null   object 
 7   Unit_Cost             1000 non-null   float64
 8   Unit_Price            1000 non-null   float64
 9   Customer_Type         1000 non-null   object 
 10  Discount              1000 non-null   float64
 11  Payment_Method        1000 non-null   object 
 12  Sales_Channel         1000 non-null   object 
 13  Region_and_Sales_Rep  1000 non-null   object 
dtypes: float64(4), int64(2), object(8)
memory usage: 109.5+ KB

``` 
Verificando se existem valores faltando: o metodo isnull() retorna um booleano True/False se o valor estiver faltando e o metodo sum() a quantidade de valores em falta por coluna.

```bash
>>> print(data_frame.isnull().sum())

Product_ID              0
Sale_Date               0
Sales_Rep               0
Region                  0
Sales_Amount            0
Quantity_Sold           0
Product_Category        0
Unit_Cost               0
Unit_Price              0
Customer_Type           0
Discount                0
Payment_Method          0
Sales_Channel           0
Region_and_Sales_Rep    0
dtype: int64

```

