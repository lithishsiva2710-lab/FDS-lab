import numpy as np
import pandas as pd

# Read the dataset
df = pd.read_csv("pre-process_datasample.csv")

print("Original Dataset:")
print(df)

# Fill missing Country with mode
df['Country'] = df['Country'].fillna(df['Country'].mode()[0])

# Fill missing Age with mean
df['Age'] = df['Age'].fillna(df['Age'].mean())

# Fill missing Salary with mean
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())

# Convert Country into dummy variables
country_dummies = pd.get_dummies(df['Country'])

# Combine dummy variables with Age, Salary and Purchased
updated_dataset = pd.concat(
    [country_dummies, df.iloc[:, [1, 2, 3]]],
    axis=1
)

# Convert Purchased into 0 and 1
updated_dataset['Purchased'] = updated_dataset['Purchased'].replace(
    ['No', 'Yes'], [0, 1]
)

print("\nPreprocessed Dataset:")
print(updated_dataset)