import numpy as np
import pandas as pd

df = pd.read_csv("Hotel_Dataset.csv")

print("Original Dataset:")
print(df)

print("\nDuplicate Rows:")
print(df.duplicated())

df.drop_duplicates(inplace=True)

index = np.array(list(range(0, len(df))))
df.set_index(index, inplace=True)

df.drop(['Age_Group.1'], axis=1, inplace=True)

# Convert columns to numeric
df['CustomerID'] = pd.to_numeric(df['CustomerID'], errors='coerce')
df['Bill'] = pd.to_numeric(df['Bill'], errors='coerce')
df['EstimatedSalary'] = pd.to_numeric(df['EstimatedSalary'], errors='coerce')

# Replace negative values with NaN
df.loc[df.CustomerID < 0, 'CustomerID'] = np.nan
df.loc[df.Bill < 0, 'Bill'] = np.nan
df.loc[df.EstimatedSalary < 0, 'EstimatedSalary'] = np.nan

# Correct hotel name
df['Hotel'] = df['Hotel'].replace('Ibys', 'Ibis')

# Correct food preference
df['FoodPreference'] = df['FoodPreference'].replace(
    ['Vegetarian', 'veg'], 'Veg'
)

df['FoodPreference'] = df['FoodPreference'].replace(
    'non-Veg', 'Non-Veg'
)

# Fill missing values
df['EstimatedSalary'] = df['EstimatedSalary'].fillna(
    round(df['EstimatedSalary'].mean())
)

df['NoOfPax'] = df['NoOfPax'].fillna(
    round(df['NoOfPax'].median())
)

df['Rating(1-5)'] = df['Rating(1-5)'].fillna(
    round(df['Rating(1-5)'].median())
)

df['Bill'] = df['Bill'].fillna(
    round(df['Bill'].mean())
)

print("\nCleaned Dataset:")
print(df)