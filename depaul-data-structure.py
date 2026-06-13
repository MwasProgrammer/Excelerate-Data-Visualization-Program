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

student_applicants = ['Reference_ID', 'First_Name', 'Last_Name', 'Email', 'Phone_Number']

# unique_applicants = df.drop_duplicates(subset=['Reference_ID'])[student_applicants]

# print(f"Unique student applicants:\n{unique_applicants}\n")

# 1. Get the absolute count of unique applications based on the Reference_ID primary key
unique_count = df['Reference_ID'].nunique()
print(f"Number of Unique Applications: {unique_count}\n")

# 2. Extract a clean list of unique applicants by removing the duplicates
# (Adjust 'Given_Name' to 'First_Name' if your dataset schema changed)
name_columns = ['Reference_ID', 'Given_Name', 'Last_Name'] 

# Drop duplicates based on Reference_ID, then isolate the name columns
unique_applicants = df.drop_duplicates(subset=['Reference_ID'])[name_columns].sum()

# 3. Display the total list of names (showing the first 20 as a preview)
# print("List of Unique Applicants:")
# print(unique_applicants.to_string(max_rows=20))

def check_internal_duplicates(cell_value):
    if pd.isna(cell_value):
        return False
    
    # Split by comma (change to ' ' or ';' if your data uses a different separator)
    tokens = [token.strip() for token in str(cell_value).split(',')]
    
    # If there are multiple words, check if compressing them into a set reduces the count
    if len(tokens) > 1:
        return len(set(tokens)) < len(tokens)
    return False

# 2. Create a boolean mask and apply it to the College column
internal_dup_mask = df['College'].apply(check_internal_duplicates)
df_college_anomalies = df[internal_dup_mask]

# 3. Output the diagnostic results
print(f"Found {len(df_college_anomalies)} rows with internally duplicated inputs in 'College'.\n")
print("Preview of affected records:")
print(df_college_anomalies[['Reference_ID', 'College']].head(10))

# Count the total number of perfectly identical rows
total_exact_dupes = df.duplicated().sum()
print(f"Total Exact Row Duplicates: {total_exact_dupes}")

# Isolate them to see what they look like
if total_exact_dupes > 0:
    exact_dupes_df = df[df.duplicated(keep=False)] # keep=False shows all copies
    print(exact_dupes_df[['Reference_ID', 'Last_Name', 'Term']].head(5))