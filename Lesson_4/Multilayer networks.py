import torch
#TODO: generate some data
torch.manual_seed(7)

#TODO: Sigmoid Function
def sigmoid(x):
    return 1/(1+torch.exp(-x))

#TODO: Features are 3 random variables
features = torch.randn((1,3))
print("features = ", features)

#TODO: Define the size of each layer in our network
n_input = features.shape[1] # Number of input units, must match number of input features
n_hidden = 2  # Number of hidden units
n_output = 1  # Number of output units

#TODO: Weights for inputs to hidden layer
W1 = torch.randn(n_input,n_output)
#TODO: Weights for hidden layer to output layer
W2 = torch.randn(n_hidden,n_output)
#TODO: and bias terms for hidden and output layers
B1 = torch.randn((1,n_hidden))
B2 = torch.randn((1,n_output))

#TODO: Calculate the output for this multi-layer network using the weights W1 & W2, and the biases, B1 & B2.
h =sigmoid(torch.mm(features,W1)+B1)
print("hidden_layer_output = ", h)
print("hidden_layer_output shape = ", h.shape)
output = sigmoid(torch.mm(h,W2)+B2)
print(output)