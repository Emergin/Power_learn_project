# this is a python library that allowa you to create visual reps of your data
# basic line plot
import matplotlib.pyplot as plt
# sample_data
x = [2,3,4,5,6,7]
y = [2,3,4,5,6,8]
# create a line plot
plt.plot(x,y)
plt.title('sample line plot')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.show()

# bar chart example 
names = ['alice', 'bob', 'charlie']
scores = [50, 70, 89]

# bar chart
plt.bar(names, scores, color='blue')
plt.title('sample barchart')
plt.xlabel('names')
plt.ylabel('scores')
plt.show()

# pie chart example 
# sample data 
activities = ['football', 'basketball', 'sleeping', 'working', 'coding', 'gaming']
hours = [2,3,8,8,2,1]

plt.pie(hours, labels=activities, autopct='%1.1f%%')
plt.title('daily activities')
plt.show()

# combine with pandas 
import pandas as pd
data = {
    'year': [2021, 2022,2023,],
    'users': [1500,3000,5000]
}
df = pd.DataFrame(data)

plt.plot(df['year'], df['users'], marker='o')
plt.title('user growth over time ')
plt.xlabel('year')
plt.ylabel('users')
plt.grid(True)
plt.show()

# practice tasks
# 1 Create a bar chart showing 5 different countries and their population.
country = ['kenya', 'uganda', 'ghana', 'nigeria']
population = [60,30,25,75]

plt.bar(country, population, color='red')
plt.title('east african countrys population in millions')
plt.ylabel('population in millions')
plt.xlabel('countries')
plt.show()

# 2 Create a pie chart showing how a student spends 24 hours of their day.
