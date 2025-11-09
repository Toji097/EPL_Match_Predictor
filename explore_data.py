import pandas as pd
import os

data_path = os.path.join('data', 'epl_final.csv')
df = pd.read_csv(data_path)

# 1️⃣ Basic info
print("Shape:", df.shape)
print("\nColumns:\n", df.columns.tolist())

# 2️⃣ Missing values check
print("\nMissing values per column:\n", df.isnull().sum())

# 3️⃣ Quick stats
print("\nBasic stats:\n", df.describe())

# 4️⃣ Unique values for FullTimeResult
print("\nUnique FullTimeResult values:", df['FullTimeResult'].unique())
