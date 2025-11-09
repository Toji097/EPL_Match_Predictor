import pandas as pd # pandas = a data analysis library, like Excel for Python (used for loading & working with data)

import os # os = built-in module for working with files, folders, and system paths

#Define the path to the dataset
data_path = os.path.join('data', 'epl_final.csv')

#Loads the dataset
df = pd.read_csv(data_path)


#Show information about the dataset
print("✅ Data loaded successfully!")
print("Shape", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nPreview:")
print(df.head())