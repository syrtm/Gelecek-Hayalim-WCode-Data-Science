# Kütüphaneleri yükleyelim
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Veriyi yükleme
data = pd.read_csv('kaggle-survey.csv')

# İlk beş satırı görüntüleyelim
print(data.head())

