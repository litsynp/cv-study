import pickle

import numpy as np
from PIL import Image


def sigmoid(x: np.ndarray) -> np.ndarray:
    return 1 / (1 + np.exp(-x))


def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y


def get_data():
    """
    Loads data from MNIST dataset and creates a `.pkl` file.
    """
    if __package__ is None:
        import sys
        from os import path
        print(path.dirname(path.dirname(path.abspath(__file__))))
        sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
        from dataset.mnist import load_mnist
    else:
        from ..dataset.mnist import load_mnist

    # Creates .pkl file in dataset directory
    # Preprocess using normalization
    (x_train, t_train), (x_test, t_test) = \
        load_mnist(flatten=True, normalize=True, one_hot_label=False)
    return x_test, t_test


def init_network():
    """
    Initializes and returns a network from `sample_weight.pkl` in current directory.
    """
    with open('sample_weight.pkl', 'rb') as f:
        network = pickle.load(f)

    return network


def predict(network, x):
    """
    Predicts (infers) that the data belongs to a certain label.
    """
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)

    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)

    a3 = np.dot(z2, W3) + b3
    y = softmax(a3)

    return y


def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()


if __name__ == '__main__':
    x, t = get_data()
    network = init_network()

    batch_size = 100  # size of batch
    accuracy_cnt = 0

    # Predict each image data saved in x with for-loop, and add up accuracy to average it
    for i in range(0, len(x), batch_size):
        # Group as a batch using range() and index slicing
        x_batch = x[i:i+batch_size]
        y_batch = predict(network, x_batch)

        # Get the index of element with the highest probability
        p = np.argmax(y_batch, axis=1)

        accuracy_cnt += np.sum(p == t[i+i+batch_size])

    # Print out ratio of correctly predicted data
    print('Accuracy: {}'.format(str(float(accuracy_cnt) / len(x))))
