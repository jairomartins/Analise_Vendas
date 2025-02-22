# Importando as bibliotecas necessárias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Carrega o arquivo CSV
data_frame = pd.read_csv('datasets/sales_data.csv')

# Exibe as 5 primeiras linhas do data_frame
#data_frame.head()

print(data_frame.head())

# Product_ID   Sale_Date Sales_Rep Region  Sales_Amount  Quantity_Sold Product_Category  Unit_Cost  Unit_Price Customer_Type  Discount Payment_Method Sales_Channel Region_and_Sales_Rep
# 0        1052  2023-02-03       Bob  North       5053.97             18        Furniture     152.75      267.22     Returning      0.09           Cash        Online            North-Bob
# 1        1093  2023-04-21       Bob   West       4384.02             17        Furniture    3816.39     4209.44     Returning      0.11           Cash        Retail             West-Bob
# 2        1015  2023-09-21     David  South       4631.23             30             Food     261.56      371.40     Returning      0.20  Bank Transfer        Retail          South-David
# 3        1072  2023-08-24       Bob  South       2167.94             39         Clothing    4330.03     4467.75           New      0.02    Credit Card        Retail            South-Bob
# 4        1061  2023-03-24   Charlie   East       3750.20             13      Electronics     637.37      692.71           New      0.08    Credit Card        Online         East-Charlie

#Obtento informações sobre o data_frame
print(data_frame.info())

# Data columns (total 14 columns):
#  #   Column                Non-Null Count  Dtype  
# ---  ------                --------------  -----  
#  0   Product_ID            1000 non-null   int64  
#  1   Sale_Date             1000 non-null   object 
#  2   Sales_Rep             1000 non-null   object 
#  3   Region                1000 non-null   object 
#  4   Sales_Amount          1000 non-null   float64
#  5   Quantity_Sold         1000 non-null   int64  
#  6   Product_Category      1000 non-null   object 
#  7   Unit_Cost             1000 non-null   float64
#  8   Unit_Price            1000 non-null   float64
#  9   Customer_Type         1000 non-null   object
#  10  Discount              1000 non-null   float64
#  11  Payment_Method        1000 non-null   object
#  12  Sales_Channel         1000 non-null   object
#  13  Region_and_Sales_Rep  1000 non-null   object
# dtypes: float64(4), int64(2), object(8)
# memory usage: 109.5+ KB



print(data_frame.describe()) # Exibe informações estatísticas sobre o data_frame

# Exibe a quantidade de valores nulos em cada coluna
print(data_frame.isnull().sum()) 

# Exibe se contem dados duplicados no data_frame
#data_frame.duplicated().sum()
print(data_frame.duplicated().sum()) 
