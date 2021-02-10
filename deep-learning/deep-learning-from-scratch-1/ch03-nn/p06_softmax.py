import numpy as np


def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y


if __name__ == '__main__':
    a = np.array([0.3, 2.9, 4.0])
    y = softmax(a)

    # Output of softmax is a real number between 0 and 1.0
    # Plus, sum of output is 1, hence output being able to be read as 'probability'
    print(y)          # [0.01821127 0.24519181 0.73659691]
    print(np.sum(y))  # 1.0
