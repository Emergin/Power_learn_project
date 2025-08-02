capital_city = {"Nepal": "kathmandu", "Kenya":"Nairobi", "Somalia": "Mogadishu", "uganda": "Kampala", "Ethiopia": "Adis ababa"}
print(capital_city)

# keys of different datatypes
numbers = {1: "one", 2:"two", 3:"three"}
print(numbers)

#adding elements to a python dictionary

print("initial dictionary", capital_city)
capital_city["japan"] = "Tokyo"
print("updated dictionary", capital_city)
numbers[4] = "four"
print("updated numbers dict", numbers)

#deleting values in a dictionary
student_id = {111:"eric", 112:"kyle", 113:"butters"}
print("initial dict", student_id)
del student_id[111]
print("updated dict", student_id)

#accessing elements in a dictionary

print(student_id[112])
name = sorted(capital_city)
print(name)
length = len(capital_city)
print(length)

#iterating through a dictionary
squares = {1:1, 2:4, 3:9, 4:16, 5:25}
for i in squares:
    print(squares[i])