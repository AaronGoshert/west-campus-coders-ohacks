import pandas as pd
import statistics
import numpy as np 

df = pd.read_csv('Iris.csv')
print(df.head())
print(df.info())

print("Species Mode")
print(statistics.mode(df['Species']))

print("Mean of Sepal")
print(np.mean(df['SepalLengthCm']))

print('Median of Sepal')
print(np.median(df['SepalLengthCm']))

print('Standard Deivation of Sepal')
print(np.sqrt(np.var(df['SepalLengthCm'], ddof=1)))

