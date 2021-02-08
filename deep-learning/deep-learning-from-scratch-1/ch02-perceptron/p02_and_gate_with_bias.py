import numpy as np

if __name__ == '__main__':
    x = np.array([0, 1])      # input
    w = np.array([0.5, 0.5])  # weight
    b = -0.7                  # bias, substituted for -theta

    print(w * x)
    print(np.sum(w * x))
    print(np.sum(w * x) + b)
