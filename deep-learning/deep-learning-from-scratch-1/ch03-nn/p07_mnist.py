import numpy as np
from PIL import Image


def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()


if __name__ == '__main__':
    # Allow imports from parent directory
    if __package__ is None:
        import sys
        from os import path
        print(path.dirname(path.dirname(path.abspath(__file__))))
        sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
        from dataset.mnist import load_mnist
    else:
        from ..dataset.mnist import load_mnist

    # Creates .pkl file in dataset directory
    (x_train, t_train), (x_test, t_test) = \
        load_mnist(flatten=True, normalize=False)

    # Print shapes of each data
    # Loads faster once .pkl file has been created
    print(x_train.shape)  # (60000, 784)
    print(t_train.shape)  # (60000,)
    print(x_test.shape)   # (10000, 784)
    print(t_train.shape)  # (60000,)

    img = x_train[0]
    label = t_train[0]
    print(label)  # 5

    print(img.shape)  # (784,)
    img = img.reshape(28, 28)  # Reshape to original shape of MNIST image
    print(img.shape)

    img_show(img)
