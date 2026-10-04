import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from category_encoders import OneHotEncoder

df = pd.read_csv('C:\\Users\\user\\AMIT\\data_analysis\\assignment_3\\insurance.csv')

categorical_columns = df.select_dtypes(include=['object']).columns
numerical_columns = df.select_dtypes(include=['int64', 'float64']).columns

df[categorical_columns] = df[categorical_columns].astype('category')
df[numerical_columns] = df[numerical_columns].astype('float64')
df.drop_duplicates(inplace=True)

# 1. Outlier Capping & Log Transform
q1 = df['bmi'].quantile(0.25)
q3 = df['bmi'].quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
df['bmi'] = df['bmi'].clip(lower=lower_bound, upper=upper_bound)
df['charges'] = np.log1p(df['charges'])

# 2. Normalization على df مباشرة
scaler = MinMaxScaler()

df[numerical_columns] = scaler.fit_transform(df[numerical_columns])
# 3. One-Hot Encoding
encoder = OneHotEncoder(cols=categorical_columns, use_cat_names=True)
df = encoder.fit_transform(df)

print(df.head())