import numpy as np

# an actual array in python:
kitkat = [344, -233, 356, 87, 879, 4, 583, 7687]
print(kitkat)

# a numpy array looks like:
snickers = np.array(kitkat)
print(snickers)

# you cannot have different data types in numpy arrays
bonobon = np.array([12, True, not False, 'yolo'])
# all the arrays haas been converted to string
print(bonobon)

# min of snickers
print(snickers.min())

# mean of snickers
print(snickers.mean())

