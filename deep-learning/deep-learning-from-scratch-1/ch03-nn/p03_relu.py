import numpy as np
import matplotlib.pyplot as plt


def relu(x: np.ndarray) -> np.ndarray:
    return np.maximum(x, 0)


if __name__ == '__main__':
    x = np.arange(-5.0, 5.0, 0.1)
    y = relu(x)

    # Graph it
    plt.plot(x, y)
    plt.show()
