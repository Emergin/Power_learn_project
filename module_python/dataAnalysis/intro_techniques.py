# understand data analysis techniques such as filtering, sorting, and aggregating data
# creating, reading and manipulating dataframes

# Series: A one-dimensional labeled array that can hold any data type (integers, strings, etc.).
# DataFrame: A two-dimensional, size-mutable, potentially heterogeneous tabular data structure with labeled axes (rows and columns).

# example 
import pandas as pd

# creating dataframe from a dictionary
data = {
    'name': ['alice', 'bob', 'charlie'],
    'age': [25,30,45],
    'city': ['Nairobi', 'kisumu', 'mombasa']
}
df = pd.DataFrame(data)
print(df)
# df = pd.read_csv('module_python/pythonLibraries/sales_data_sample.csv')

# manipulating dataframes
# selecting columns
print(df['age'])
# filter rows 
print(df[df['age'] > 30])
df['country'] = ['usa', 'usa', 'usa']
print(df)
df.drop('country', axis=1, inplace=True)
print(df)

