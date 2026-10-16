import numpy as np
import pandas as pd

list1 = [
    [1, 'Smith', 50000],
    [2, 'Jones', 60000]
]

df = pd.DataFrame(list1)

print("Original DataFrame:")
print(df)

df.columns = ['Empd', 'Name', 'Salary']

print("\nDataFrame with Column Names:")
print(df)

print("\nDataFrame Information:")
df.info()


df = pd.read_csv("employee.csv")

print("First 5 Records:")
print(df.head())

print("\nLast 5 Records:")
print(df.tail())

print("\nDataFrame Information:")
df.info()

print("\nSalary:")
print(df.salary)

print("\nType of Salary:")
print(type(df.salary))

print("\nMean Salary:")
print(df.salary.mean())

print("\nMedian Salary:")
print(df.salary.median())

print("\nMode Salary:")
print(df.salary.mode())

print("\nSalary Variance:")
print(df.salary.var())

print("\nSalary Standard Deviation:")
print(df.salary.std())

print("\nStatistical Description:")
print(df.describe())

print("\nDescription Including All Columns:")
print(df.describe(include='all'))

print("\nColumn Names:")
empCol = df.columns
print(empCol)

print("\nData as Array:")
emparray = df.values
print(emparray)

print("\nEmployee DataFrame from Array:")
employee_DF = pd.DataFrame(emparray, columns=empCol)
print(employee_DF)