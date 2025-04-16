import math
import numpy as np
import random as rand

test = np.random.rand(5)
print(test)

def sigmoid(x):

    x = np.array(x)
    return 1 / (1 + np.exp(-x))

print(sigmoid(test))

def softmax(x):

  return np.exp(x) / np.sum(np.exp(x))

print(softmax(test))

def relu(x):

  ans = np.maximum(x, test)
  return ans

print(relu(test))

