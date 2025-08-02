string1 = 'python programming'
string2 = 'welcome to power learn project july'

#accessing string caharacters in python
print(string1[1])
print(string1[-4])

#python strings are immutable meaning they cant be changed 
# however we can assign the variable name a new string 
string1 = 'we changed the string'

#multiline string
message = ''' 
never stop watching movies
never stop dreaming big
'''
print(message)

# python string operations
#compare 2 strings
str1 = 'welcome to our home'
str2 = 'how are you?'
str3 = 'how is today?'
print(str1 == str2)

#join 2 or more strings
greet = 'hello'
name = 'jack'
result = greet + name
print(result)

#iterate through a python string

program = 'iteration is using a for loop'
for i in program:
    print(i)

#python string length
print('the length is', len(program))

#string membership test
print('a' in 'program')
print('at' not in 'battle')
new = program.upper()
print(new)