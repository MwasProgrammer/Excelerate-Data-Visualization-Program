import pandas as pd
import numpy as np

# pd_set_option = pd.set_option('display.max_columns', None)
# pd_set_option = pd.set_option('display.max_rows', None)
# pd_set_option = pd.set_option('display.width', 1000)

df = pd.read_csv("DePaul_Data+-+DePaul_Data.csv")

print(f"Total rows: {df.shape[0]}") 
print(f"Total columns: {df.shape[1]}\n")

print(f"Total entries: {df.size} \n")

total_missing_values = df.isnull().sum().sum()
print(f"Total missing values: {total_missing_values} \n")

print(f"Missing values (Null) Percentage: {total_missing_values / df.size * 100:.2f}% \n")

print(f"Missing values per column:\n{df.isnull()} \n")

schema_data_type_report = pd.DataFrame ({
    'Valid Entries': df.count(),
    'Data Type': df.dtypes,
    'Missing Entries (Null)': df.isnull().sum(),

})

with pd.option_context('display.max_rows', None):
    print(f"Data Type Report:\n{schema_data_type_report}\n")


print(f"Unique Reference_ID:{df['Reference_ID'].is_unique} \n")

print(f"Unique Reference_ID count: {df['Reference_ID'].nunique()} \n")

print(f"Duplicate Reference_ID count: {df['Reference_ID'].duplicated()} \n")

print(f"Unique Application: {df['Reference_ID', 'First_Name', 'Last_Name'].is_unique} \n")
