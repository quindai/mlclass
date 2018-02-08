import pandas as pd
import numpy as np

#https://chrisalbon.com/python/data_wrangling/pandas_missing_data/
data = pd.read_csv('diabetes_dataset_0.csv')
df = pd.DataFrame(data)
#df1 = pd.DataFrame(pd.read_csv('diabetes_app.csv'))
print df.keys()

#feature_cols = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness',
#                'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']

df = df.fillna(0)
glucose = df.Glucose.mean()
bloodmean = df.BloodPressure.mean()
skinthickmean = df.SkinThickness.mean()
bmimean = df.BMI.mean()
insulinmean = df.Insulin.mean()
##df['BloodPressure'] = [bloodmean if x == 0 for x in df['BloodPressure']]
df['BloodPressure'].replace(0, bloodmean, inplace=True)
df['SkinThickness'].replace(0, skinthickmean, inplace=True)
df['BMI'].replace(0, bmimean, inplace=True)
df['Insulin'].replace(0, insulinmean, inplace=True)
df['Glucose'].replace(0, insulinmean, inplace=True)
print df.SkinThickness
#df = df.drop('SkinThickness', 1)
#df = df.drop(df.columns[[0]], axis=1)
#print df
df.to_csv('diabetes_dataset.csv', sep=',')

#df1 = df1.drop('SkinThickness', 1)
#df1.to_csv('diabetes_app.csv', sep=',')
#print df1

#print data.keys()

#for dado in data.BloodPressure:
#    data.BloodPressure
#as colunas podem ser acessadas usando o cabecario
#print (data.Outcome)