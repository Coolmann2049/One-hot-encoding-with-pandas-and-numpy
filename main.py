import numpy as np
import pandas as pd
file_path = "C:\\Users\Pc\Downloads\\francedataset.csv"

#making dataframe
df = pd.read_csv(file_path)
df = df.drop(['Date and Hour','Date'],axis = 1)

# getting object columns
s = (df.dtypes == 'object')
object_cols = list(s[s].index)

#creating a copy to not change the original database
df1 = df.copy()
df2 = df.copy()

#one-hot encoding
for col in object_cols:
    unique_vals = df1[col].unique() #gets a list of all the unique values in a column

        # here we get a unique column name for every single combination of value and column
    for val in unique_vals:
        new_col_name = f'{col}_{val}'
        df1[new_col_name] = np.where(df1[col] == val, 1, 0)  # we create a new column in df1 that get filled with np.where function
    df1 = df1.drop(col,axis = 1)
df1.to_csv("ohencoder.csv")

#df1 is now one-hot-encoded.

#for ordinal encoding
mapping = {}

for col in object_cols:
        # Get unique categories in the column and sort them (optional)
        unique_vals = np.unique(df2[col])

        #we make a dictionary with key being columns and the value being another
        #dictionary that has key value pairs as its unique value and index
        mapping[col] = {val: idx for idx, val in enumerate(unique_vals)}

        #.map() is a function that replaces all the column values with new values
        df2[col] = df2[col].map(mapping[col])
print(mapping)

df2.to_csv("Ordinalencoder.csv")

#df2 is now ordinal encoded.