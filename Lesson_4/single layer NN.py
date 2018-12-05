import torch

def sigmoid(x):
    return 1/(1 + torch.exp(-x))
#TODO: Generate some data
torch.manual_seed(7) #set the random seed to things are predictable

#TODO: Feature are 5 random normal variables randn
features = torch.randn((1,5)) #1 row, 5 columns
#TODO: True weights for our data, random normal variables again
weights = torch.randn_like(features)
#TODO: A true bias term
bias = torch.randn((1,1))
#TODO: ## Calculate the output of this network using the weights and bias tensors
y = sigmoid(torch.sum(weights*features)+bias)
print("y = {}".format(y))

#TODO: Reshaping
# print("weights size = {} \nfeatures size = {}".format(weights.shape,features.shape))
# print("---------------------------Reshape---------------------------")
# print(weights)
# print(weights.reshape(5,1))
#
# print("---------------------------View---------------------------")
# print(weights)
# print(weights.view(5,1))
#
# print("---------------------------Resize---------------------------")
# print(weights)
# print(weights.resize_(5,1)) #TODO: _ in-place tuc la no se thay doi luon ma ko can gan
# print(weights)

#TODO: Calculate the output of this network using matrix multiplication
y = sigmoid(torch.mm(features,weights.view(5,1)) + bias)
print(y)