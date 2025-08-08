students_id = {112, 113, 114, 115, 116}
print(students_id)
vowel_letters = {"a",'e','i','o','u'}
print(vowel_letters)
mixed_set = {"hello",1,2,'welcome'}
print(mixed_set)

#creating an empty set using the set() function
empty_set = set()

#empty dictionary 
empty_dict = { }

#trying duplicate items ina set
numbers = {2,3,4,2,3,4,5,6,7,7}
print(numbers)

#add and update items in a set

print("initial set", numbers)
numbers.add(32)
print("updated set", numbers)

#update() items in a set

companies = {'lacoste', 'safaricom', 'airtel'}
tech_companies = {'microsoft', 'google', 'amazon'}
companies.update(tech_companies)
print(companies)

#remove an element from a set
languages = {'swift', 'c++', 'javascript', 'python'}
print("initial set", languages)
removed_value = languages.discard('javascript')
print('set after remove', languages)
new = max(numbers)
print(new)

#iteration over a set in python

for number in numbers:
    print(number)

fruits = {'apple', 'kiwi', 'oranges'}
for fruit in fruits:
    print(fruits)

# find number of set elements
even_numbers = {2,3,4,5,6,7,8}
print("set:", even_numbers)
print("total elements", len(even_numbers))

#union of 2 sets 
A = {1,2,3,4,5}
B = {4,5,6,7,8}
print('union using |', A | B)
print('union using union()', A.union(B))

#intersection of set elemets 
print('intersectio using &', A & B)
print('intersection using intersection(): ', A.intersection(B))

#differrence of set elements
print('difference using -: ', A - B)
print('difference using difference(): ', A.difference(B))

#symmetric_difference of set elements
print('symmetric_difference using ^: ', A ^ B)
print('symmetric_difference using symmetriic_difference(): ', A.symmetric_difference(B))

#check if 2 sets are equal 
if A == B:
    print('set A and B are equal')
else:
    print('set A and set B are not equal')