# pandas is used for data manipulation and analysis
# it allows you to work with tables, clean and filter easily, read from csv etc
# basic pandas example 
import pandas as pd
import numpy as np
# create a dataframe
data = {
    'name': ['alice', 'bob', 'mary'],
    'age': [23,34,56],
    'score': [84, 54, 76]
}
df = pd.DataFrame(data)
print(df)

# access columns
print('names', df['name'])
# filter rows
print('scores above 60')
print(df[df['score'] > 60])

# reading csv  files with pandas 

# df = pd.read_csv('module_python/pythonLibraries/sales_data_sample.csv')
# print(df.head()) # show the first 5 rows

# practice task
frame1 = {
    'name': ['student1', 'student2', 'student3'],
    'age': [23,24,25],
    'grade': ['A', 'B', 'c']
}

df['passed'] = df['grade'] > 50
df = pd.DataFrame(frame1)

print(df)