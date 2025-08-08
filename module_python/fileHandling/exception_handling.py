# basic stucture of of try - except blocks
# try - runs code that might have error 
# except - catches the error allows you to handle it without crashing 
# example 
# try:
#     with open("fileHandling/example.txt", 'r')as file:
#         data = file.read()
# except FileNotFoundError:
#     print('file not found please check file name')

# advanced file handling with finnaly and custome errors
try:
    with open('fileHandling/example.txt', 'w') as file:
        file.write('another update on file handling now am rewriting this using try except blocks for file handling and using finally')
except FileNotFoundError:
    print('file not found please check filename')
finally:
    file.close()