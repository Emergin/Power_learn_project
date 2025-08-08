# numpy - or numerical python
# used for working large arrays and performing math operations

# installing numpy 
# pip install numpy

# basic numpy example 
import numpy as np
my_array = np.array([1,2,3,4,5,6,7,8,9])
print(my_array)

# perform operations
print('array * 2', my_array * 2)
print('mean: ', np.mean(my_array))
print('square roots: ', np.sqrt(my_array))

# practice task
my_second_array = np.array([x for x in range(10, 50)])
max_number = np.max(my_second_array)
min_number = np.min(my_second_array)
result = my_second_array * 3

print(f'this is my tasks practice using numpy: \n my array is: {my_second_array} \n maximum number is: {max_number} \n minimum number is: {min_number} \n the result of multiplying everything by 3 is \n {result}')
