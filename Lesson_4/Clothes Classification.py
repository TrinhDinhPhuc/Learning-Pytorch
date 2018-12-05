import torch
from torchvision import datasets,transforms
from Lesson_4.helper import *

#Define a transform to normalize the data
transform = transforms.Compose([transforms.ToTensor(),
                                transforms.Normalize((0.5,0.5,0.5),(0.5,0.5,0.5))])
#Download and load the trainning data
trainset = datasets.FashionMNIST('~/.pytorch/F_MNIST_data',download=True,train=True,transform=transform)
trainloader  = torch.utils.data.DataLoader(trainset,batch_size=64,shuffle=True)

#Download and load the test data
testset = datasets.FashionMNIST('~/.pytorch/F_MNIST_data',download=True,train=False,transform=transform)
testloader  = torch.utils.data.DataLoader(testset,batch_size=64,shuffle=True)
image , label = next(iter(trainloader))
imshow(image[0,:])