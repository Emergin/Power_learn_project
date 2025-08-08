name = input('enter the name of the file example (input.txt)  use this format: ')
try:
    with open(f'fileHandling/{name}', 'r') as file:
        data = file.read()
        print(data)
except FileNotFoundError:
    print('file not found')
except PermissionError:
    print('file cant be opened')
except Exception as e:
    print('an error occured')
