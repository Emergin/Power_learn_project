with open('fileHandling/input.txt', 'w') as file:
    file.write('am going to save this month' '\n'
    'where are you going?' '\n'
    'Am not available right now' '\n'
    'Am currently learning file handling' '\n'
    'Python is a programming language not a snake')

try:
    with open('fileHandling/input.txt', 'r') as file:
        read = file.read()
        words = read.split()
        word_count = len(words)
        upper = read.upper()
        print(upper)
        print(words)

        with open('fileHandling/output.txt', 'w') as file:
            file.write(f'processed text \n {upper} \n and the word count is \n {word_count}')
        print('new file created successfully')
except:
    print('file not found!')
finally:
    file.close()