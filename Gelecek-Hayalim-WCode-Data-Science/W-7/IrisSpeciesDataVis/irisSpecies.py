import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('Iris.csv')

print(data.head())
print(data.describe())
print(data.columns)

print(data.isnull().sum())


sns.pairplot(data, hue='Species')
plt.title('Iris Özelliklerinin Dağılımı')
plt.show()

sns.boxplot(data=data, x='Species', y='SepalLengthCm')
plt.title('Sepal Uzunluğuna Göre Türlerin Dağılımı')
plt.show()