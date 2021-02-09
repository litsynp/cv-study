import numpy as np
import matplotlib.pyplot as plt


def sigmoid(x: np.ndarray) -> np.ndarray:
    return 1 / (1 + np.exp(-x))


if __name__ == '__main__':
    x = np.arange(-5.0, 5.0, 0.1)
    y = sigmoid(x)

    # Graph it
    plt.plot(x, y)
    plt.ylim(-0.1, 1.1)  # Set y-axis boundaries
    plt.show()
