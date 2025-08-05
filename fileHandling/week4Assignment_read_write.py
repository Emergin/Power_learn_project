try:
    with open('fileHandling/assignment1.txt', 'r') as file:
        data = file.read()
    with open('fileHandling/modified.txt', 'w') as file:
        file.write('The assignment file has been overwriten with this file' '\n'
        'This is the new modified file' '\n'
        'it has been created automatically using the write() finction')
except:
    print('file not found!!')
finally:
    file.close()