import numpy as np


def NAND(x1, x2):
    # the only differences from AND gate are w and b
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7

    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1


def OR(x1, x2):
    # the only differences from AND gate are w and b
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2

    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1


if __name__ == '__main__':
    print(NAND(0, 0))  # 0
    print(NAND(1, 0))  # 0
    print(NAND(0, 1))  # 0
    print(NAND(1, 1))  # 1
