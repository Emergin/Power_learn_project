languages = ['Python', 'Java', 'C++', 'JavaScript']
print(languages[-1])
my_list = ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z']
print(my_list[2:5])
print(my_list[5:])

# appending elements
numbers = [1, 2, 3]
print("before append:", numbers)
numbers.append(4)
print("after append:", numbers)

#extend method
prime_numbers = [2, 3, 5]
print("before extend:", prime_numbers)
prime_numbers.extend([7, 11, 13])
print("after extend:", prime_numbers)

# change list items, elements
fruits = ['apple', 'banana', 'cherry']
print("before change:", fruits)
fruits[1] = 'orange'
print("after change:", fruits)
fruits[0] = 'kiwi'
print("after another change:", fruits)

# removing elements
vegetables = ['carrot', 'potato', 'cabbage']
print("before remove:", vegetables)
vegetables.remove('potato')
print("after remove:", vegetables)

#iterating through a list
list1 = [1, 2, 3, 4,5]
for item in list1:
    print(item)

# iteration2 
books = ['book1', 'book2', 'book3']
for items in books:
    print(items)

#python list comprehension
numbers = [number*number for number in range(1, 6)]
print(numbers)