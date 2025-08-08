# a syntax for creating a list by evaluating an expression 
# syntax [expression for item in iterable if condition]
# expression - the value or transformation applied to each element
# item - a variable that represent each element in an iterable
# iterable - like a list 
# condition - a filter that determines whether to include an element

# example 
squares = []
for x in range(1, 5):
    squares.append(x**2)

# #list comprehension
squares = [x**2 for x in range(10)]
even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)
print(squares)

# create a 3 x 3 matrix using nested list comprehension
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(matrix)

#transforming data 
names  = ["alice", "bob", "dan"]
uppercased_names = [name.upper() for name in names]
print(uppercased_names)

# filtering data 
data = [12, 34, 56, 78, 98, 22, 15, 50, 35]
divisible_by_5 = [num for num in data if num % 5 == 0]
print(divisible_by_5)