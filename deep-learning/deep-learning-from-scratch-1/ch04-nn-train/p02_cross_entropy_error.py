import numpy as np


def cross_entropy_error(y, t):
    delta = 1e-7
    return -np.sum(t * np.log(y + delta))


# The answer is '2'
t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]


# e.g. 1) Assume that it's most likely to be '2' (0.6)
y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
print(cross_entropy_error(np.array(y), np.array(t)))  # 0.510825457099338

# e.g. 2) Assume that it's most likely to be '7' (0.6)
y = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]
print(cross_entropy_error(np.array(y), np.array(t)))  # 2.302584092994546
