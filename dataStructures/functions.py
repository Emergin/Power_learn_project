#syntax of functions in python

# def function_name(parameters):
#optional comments 
#code block 
#return value

# defining and calling a function
def greet_name(name):
    """greet a person by their name"""
    return f"hello {name} "
print(greet_name("alice"))

# parameters and arguments
def add(a, b):
    return a + b
print(add(1, 2))

#default arguments
def greet(name="guest"):
    return f"hello {name}"
print(greet())
print(greet("alice"))

#keyword arguments
def introduce(name, age):
    return f"my name is {name}, and i'm {age} years old"
print(introduce(name = "alice", age = 23))

#anonymous functions : lambda
add = lambda x, y: x + y
print(add(2, 3)) 

#using lambda with map()
numbers1 = [1,2,3,4,5]
double  = list(map(lambda x: x ** 2, numbers1))
print(double)

#recursive functions
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
print(factorial(5))