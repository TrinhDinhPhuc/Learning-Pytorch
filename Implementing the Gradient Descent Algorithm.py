import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv("C:\\Users\\PhucCoi\\PycharmProjects\\Pytorch\\deep-learning-v2-pytorch-master\\intro-neural-networks\\gradient-descent\\data.csv",header=None)
X = np.array(data[[0,1]])
y = np.array(data[2])
def plot_points(X,y):
    #TODO: argwhere nay de loc tat ca cac vi tri trong array = 1
    admitted = X[np.argwhere(y==1)]
    #TODO: argwhere nay de loc tat ca cac vi tri trong array = 0
    rejected = X[np.argwhere(y==0)]
    plt.scatter([s[0][0] for s in rejected],[s[0][1] for s in rejected],s = 25, color = 'blue',edgecolors='k')
    plt.scatter([s[0][0] for s in admitted],[s[0][1] for s in admitted],s = 25, color = 'red',edgecolor = 'k')
def display(m, b, color='g--'):
    plt.xlim(-0.05,1.05)
    plt.ylim(-0.05,1.05)
    x = np.arange(-10, 10, 0.1)
    plt.plot(x, m*x+b, color)
#plot_points(X,y)
#plt.show()
#----------------------------------------------------------------------
#TODO: Sigmoid activation fucntion
def sigmoid_func(x):
    return 1/(1+np.exp(-x))
#TODO: Output (prediction) formula
def y_hat_formula(weights, features,bias):
    return sigmoid_func(np.dot(features, weights) + bias)
#TODO: Error Function - Error (log-loss) formula
def error_func(y,y_hat):
    return -y*np.log(y_hat) - (1-y)*np.log(1-y_hat)
#TODO: Function that updates weights
def update_weight(x,y,weights,bias,learnrate):
    y_hat = y_hat_formula(weights=weights,features=x,bias=bias)
    d_error = y-y_hat
    weights += learnrate*d_error*x
    bias += learnrate * d_error
    return weights,bias
#---------------------------------------------------------------------------------
#TODO: Training function
np.random.seed(44)
epochs = 100
learnrate = 0.01
def train(features, targets, epochs,learnrate, graph_lines = False):
    errors = []
    n_records , n_features = features.shape
    last_loss = None
    weights = np.random.normal(scale = 1/n_features**.5, size = n_features)
    bias = 0
    for e in range(epochs):
        dew_w = np.zeros(weights.shape)
        for x, y in zip(features, targets):
            y_hat = y_hat_formula(weights=weights,features=x,bias=bias)
            error = error_func(y,y_hat)
            weights,bias = update_weight(x,y,weights,bias,learnrate)
        # Printing out the log-loss error on the training set
        out = y_hat_formula(features=features,weights=weights,bias=bias)
        loss = np.mean(error_func(targets,out))
        errors.append(loss)
        if e % (epochs/10)==0:
            print("\n========== Epoch", e,"==========")
            if last_loss and last_loss < loss:
                print("Train loss: ", loss, "  WARNING - Loss Increasing")
            else:
                print("Train loss: ", loss)
            last_loss = loss
            predictions = out > 0.5
            accuracy = np.mean(predictions == targets)
            print("Accuracy: ", accuracy)
        if graph_lines and e % (epochs / 100) == 0:
            display(-weights[0]/weights[1], -bias/weights[1])
    # Plotting the solution boundary
    plt.title("Solution boundary")
    display(-weights[0]/weights[1], -bias/weights[1], 'black')

    # Plotting the data
    plot_points(features, targets)
    plt.show()

    # Plotting the error
    plt.title("Error Plot")
    plt.xlabel('Number of epochs')
    plt.ylabel('Error')
    plt.plot(errors)
    plt.show()

train(X, y, epochs, learnrate, True)