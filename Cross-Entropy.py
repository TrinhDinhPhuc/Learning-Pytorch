import numpy as np

# TODO: Write a function that takes as input two lists Y, P, and returns the float corresponding to their cross-entropy.
'''
Eg: CE[(1,1,0),(0.8,0.7,0.1)]
np.log is ln, whereas np.log10 is your standard base 10 log.

'''
def cross_entropy(Y, P):
    _sum = 0
    for y_i, P_i in zip(Y,P):
        _sum += -(y_i*np.log(P_i)+(1-y_i)* np.log(1-P_i))
    return _sum
# TODO: Luu y ta co the dung truc tiep List de cong tru nhan chia voi dieu kien la cung List cung len()
def cross_entropy_sol(Y, P):
    Y = np.float_(Y) #convert to float type
    P = np.float_(P) #convert to float type
    print(Y,P)
    return -np.sum(Y * np.log(P) + (1 - Y) * np.log(1 - P))
if __name__ == '__main__':
    print(cross_entropy([1,0,1,1],[0.4,0.6,0.1,0.5]))
    print(cross_entropy_sol([1,0,1,1],[0.4,0.6,0.1,0.5]))

'''
Trying for Y=[1,0,1,1] and P=[0.4,0.6,0.1,0.5].
The correct answer is: 4.8283137373
'''