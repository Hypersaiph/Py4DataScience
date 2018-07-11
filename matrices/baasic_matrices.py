# m[x,y]
# x is a row
# y is a column

import numpy as np

data = np.arange(0, 20)

# fill by row
matrix_a = np.reshape(data, (5, 4), 'C')
print(matrix_a)

# fill by column
matrix = np.reshape(data, (5, 4), 'F')
print(matrix)

# printing element 2, 2
print(matrix_a[2, 2])

# reshaping
row_1 = ["I", "am", "happy"]
row_2 = ["what", "a", "day"]
row_3 = ['1', '2', '3']

# making an array
print(np.array([row_1, row_2, row_3]))

