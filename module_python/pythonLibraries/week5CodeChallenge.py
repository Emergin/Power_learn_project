import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import requests as rq

my_array = np.array([1,2,3,4,5,6,7,8,9])
mean1 = np.mean(my_array)
print(mean1)

data = pd.DataFrame(my_array)
print(data)

# dataset = pd.read_csv('data.csv')
# print(dataset.head())
response = rq.get('https://catfact.ninja/fact')
print(response.json()['fact'])

list1 = [1,2,3,4,5]
list2 = [5,6,7,8,9]
plt.plot(list1,list2)
plt.title('simple line graph')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.show()