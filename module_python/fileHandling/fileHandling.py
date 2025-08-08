# file operations in python 
# opening files 
# use open() in python
# syntax open(filename, mode)
# modes include # 
# 'r' read mode 
# 'w' creates a new file or overwrites an existing one 
# 'a' append mode adds new data without deleting the existing one 
# 'rb', and 'wb' binary modes for non-text files like images
# example 
# file = open('dataStructures/example.txt', 'r')

# reading files 
# .read() reads the entire file
# .readline() reads a single line at a time
# .readlines reads all lines and returns a list

# example 
# with open("dataStructures/example.txt", 'r') as file:
#     data = file.read()
#     print(data)


# writing or appending files 
# write() overwrites content while append() allows adding without deleting 
# example 
# with open("dataStructures/example.txt", 'w') as file:
#     file.write("this is me practising how to use write() in file handling using python")

try:
    with open("fileHandling/example.txt", 'a') as file:
        file.append("Hello there using append()")
except:
    print('file not found')
finally:
    file.close()