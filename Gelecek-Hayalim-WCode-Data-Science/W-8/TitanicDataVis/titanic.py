import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('Titanic-Dataset.csv')

print(data.head())
print(data.describe())
print(data.columns)
print(data.isnull().sum())

sns.countplot(data=data, x='Survived')
plt.title('Survival Count (0 = No, 1 = Yes)')
plt.show()

sns.countplot(data=data, x='Survived', hue='Sex')
plt.title('Survival Count by Gender')
plt.show()

sns.boxplot(data=data, x='Survived', y='Age')
plt.title('Survival by Age')
plt.show()

sns.scatterplot(data=data, x='Fare', y='Age', hue='Survived')
plt.title('Fare(bilet ücreti) ve Yaş Arasındaki İlişki')
plt.show()