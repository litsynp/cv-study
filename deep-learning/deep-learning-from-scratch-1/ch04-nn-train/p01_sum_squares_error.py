import numpy as np


def sum_squares_error(y, t):
    return 0.5 * np.sum((y - t) ** 2)


# The answer is '2'
t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]


# e.g. 1) Assume that it's most likely to be '2' (0.6)
y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
print(sum_squares_error(np.array(y), np.array(t)))  # 0.09750000000000003

# e.g. 2) Assume that it's most likely to be '7' (0.6)
y = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]
print(sum_squares_error(np.array(y), np.array(t)))  # 0.5975
