import numpy as np
counter = 0 
quiz_choices = [[1,1], [2,4], [5,-5], [-4,5]]

for i in quiz_choices:
    counter += 1
    input_x = i # inputs x1 and x2
    score = 4 * input_x[0] + 5*input_x[1] - 9 # this would be our "neuron": w*x +b = y
    sig_fn = 1 / (1+ np.exp(-score)) ## np.exp(x) = e^x
    print("Option %s " % (counter))
    print("\t The raw score is ", score)
    print("\t The probability is ", sig_fn)
