import numpy as np
import matplotlib.pyplot as plt


def step_function(x: np.ndarray) -> np.ndarray:
    return np.array(x > 0, dtype=int)


if __name__ == '__main__':
    x = np.arange(-5.0, 5.0, 0.1)
    y = step_function(x)

    # Graph it
    plt.plot(x, y)
    plt.ylim(-0.1, 1.1)  # Set y-axis boundaries
    plt.show()
