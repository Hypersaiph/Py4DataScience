import numpy as np
from numpy.random import randn

# print(randn())


x = randn()
answer = None
if x > 1:
    answer = "x is greater than 1"
elif x >= -1:
    answer = "x is between -1 and 1"
else:
    answer = "x is less than 1"
print(x)
print(answer)
