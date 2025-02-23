import pandas as pd


df=pd.read_csv("./dataset/Titanic-Dataset.csv")

df.fillna({'Age':df['Age'].median(),'Embarked':df['Embarked'].mode()[0]},inplace=True)

df.to_csv("./dataset/clean_titanic_dataset.csv", index=False)

print("Datset cleaned")