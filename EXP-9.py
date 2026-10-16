import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Read the dataset
data = pd.read_csv("Iris_Dataset.csv")

print(data)

# Display information
print("\nDataset Information:")
print(data.info())

# Statistical description
print("\nStatistical Description:")
print(data.describe())

# Count each variety
print("\nVariety Count:")
print(data.value_counts("variety"))

# Count plot
sns.countplot(x='variety', data=data)
plt.show()

# One-hot encoding
dummies = pd.get_dummies(data.variety)

FinalDataset = pd.concat(
    [pd.get_dummies(data.variety),
     data.iloc[:, [0, 1, 2, 3]]],
    axis=1
)

print("\nFinal Dataset:")
print(FinalDataset.head())

# Scatter plot - Sepal
sns.scatterplot(
    x='SepalLengthCm',
    y='SepalWidthCm',
    hue='variety',
    data=data
)
plt.show()

# Scatter plot - Petal
sns.scatterplot(
    x='PetalLengthCm',
    y='PetalWidthCm',
    hue='variety',
    data=data
)
plt.show()

# Pair plot
sns.pairplot(data, hue='variety', height=3)
plt.show()

# Histogram - Petal Length
sns.FacetGrid(
    data,
    hue='variety',
    height=5
).map(
    sns.histplot,
    'PetalLengthCm'
).add_legend()
plt.show()

# Histogram - Petal Width
sns.FacetGrid(
    data,
    hue='variety',
    height=5
).map(
    sns.histplot,
    'PetalWidthCm'
).add_legend()
plt.show()

# Histogram - Sepal Length
sns.FacetGrid(
    data,
    hue='variety',
    height=5
).map(
    sns.histplot,
    'SepalLengthCm'
).add_legend()
plt.show()

# Histogram - Sepal Width
sns.FacetGrid(
    data,
    hue='variety',
    height=5
).map(
    sns.histplot,
    'SepalWidthCm'
).add_legend()
plt.show()