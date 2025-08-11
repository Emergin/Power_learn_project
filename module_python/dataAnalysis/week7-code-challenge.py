import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('/home/trubel/Documents/Github/Power_learn_project/module_python/dataAnalysis/sales_data.csv')

df = pd.DataFrame(data)
print(df)
total_revenue = df['Revenue ($)'].sum()
print(f'total revenue is:', total_revenue)
# best selling product based on quantity sold
best_selling_product = data.loc[data['Quantity-Sold'].idxmax(), 'Product']
print(f'best selling product is: ', best_selling_product)
day_with_highest_sales = data.loc[data['Quantity-Sold'].idxmax(), 'Date (YYYY-MM-DD)']
print(f'the day with the highest sales is: ', day_with_highest_sales)

with open('module_python/dataAnalysis/output.txt', 'w') as file:
    file.write(f'sales summary report')
    file.write(f'===============================\n')
    file.write(f'total revenue is {total_revenue} \n')
    file.write(f'best selling product is {best_selling_product} \n')
    file.write(f'the day with the highest sales is {day_with_highest_sales} \n')
    print('results saved sucessfully')
