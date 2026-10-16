import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load tips dataset
tips = sns.load_dataset('tips')

# Display first 5 records
print("First 5 Records:")
print(tips.head())

# Statistical description
print("\nStatistical Description:")
print(tips.describe())

# Distribution plot
sns.displot(tips.total_bill, kde=True)
plt.show()

# Joint plot
sns.jointplot(x=tips.tip, y=tips.total_bill)
plt.show()

# Regression joint plot
sns.jointplot(x=tips.tip, y=tips.total_bill, kind="reg")
plt.show()

# Pair plot
sns.pairplot(tips)
plt.show()

# Count values of time
print("\nTime Value Counts:")
print(tips.time.value_counts())

# Pair plot based on time
sns.pairplot(tips, hue='time')
plt.show()