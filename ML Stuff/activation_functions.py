import math
import numpy as np
import random as rand

test = np.random.rand(5)
print(test)

# output range: (0,1) best used for Binary Classification output layer)
def sigmoid(x):

    x = np.array(x)
    return 1 / (1 + np.exp(-x))

print(sigmoid(test))

# output range: (0,1) sums to 1, multiclass classification
def softmax(x):

  return np.exp(x) / np.sum(np.exp(x))

print(softmax(test))

# output range: [0,∞), best used for Most hidden layers in deep networks
def relu(x):

  ans = np.maximum(x, test)
  return ans

print(relu(test))

# model type: Linear Regression   |  Activation Function: None
#             Logistic Regression |  Activation Function: Sigmoid
#             Neural Networks     |  Activation Function: ReLu (hidden layers), Sigmoid/Softmax (output layers)
