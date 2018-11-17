import numpy as np

# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def softmax(L):
    return np.exp(L)/(sum(np.exp(L)))
print(softmax([5,6,7]))

def softmax_c2(L):
    expL = np.exp(L)
    sumExpL = sum(expL)
    result = []
    for i in expL:
        result.append(i*1.0/sumExpL)
    return result
'''
Trying for L=[5,6,7].
The correct answer is
[0.09003057317038046, 0.24472847105479764, 0.6652409557748219]
And your code returned
[0.09003057 0.24472847 0.66524096]

Correct!
'''