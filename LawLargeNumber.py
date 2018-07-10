# LLN

# prove if the law of large numbers satisfies a anormal distribution
# mean = 0, stdev = 1
# the answer should be close to 68.2%
import numpy as np
from numpy.random import randn

N = 10000
counter = 1
for i_the_AI in randn(N):
    if (i_the_AI > -1 and i_the_AI < 1):
        counter = counter + 1
answer = counter / N
print(answer)
# f*ck yes its amazing
