import pandas as pd
DROP_COLS=['PassengerId','Name','Ticket']
clos_categorical_cols=['Sex','Embarked']
df=pd.read_csv('titanic.csv')
df[clos_categorical_cols] = df[clos_categorical_cols].astype('category')