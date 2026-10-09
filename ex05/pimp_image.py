import numpy as np
import matplotlib.pyplot as plt


def _show(array: np.ndarray, title: str) -> None:
    """Display an image with a title."""
    plt.imshow(array)
    plt.title(title)
    plt.show()


def ft_invert(array) -> np.ndarray:
    """Inverts the color of the image received."""
    result = 255 - array
    _show(result, "Invert")
    return result


def ft_red(array) -> np.ndarray:
    """Keeps only the red channel of the image received."""
    result = array.copy()
    result[:, :, 1] = result[:, :, 1] * 0
    result[:, :, 2] = result[:, :, 2] * 0
    _show(result, "Red")
    return result


def ft_green(array) -> np.ndarray:
    """Keeps only the green channel of the image received."""
    result = array.copy()
    result[:, :, 0] = result[:, :, 0] - array[:, :, 0]
    result[:, :, 2] = result[:, :, 2] - array[:, :, 2]
    _show(result, "Green")
    return result


def ft_blue(array) -> np.ndarray:
    """Keeps only the blue channel of the image received."""
    result = array.copy()
    result[:, :, 0] = 0
    result[:, :, 1] = 0
    _show(result, "Blue")
    return result


def ft_grey(array) -> np.ndarray:
    """Converts the image received to greyscale."""
    grey = array[:, :, 0] / 3 + array[:, :, 1] / 3 + array[:, :, 2] / 3
    result = array.copy()
    result[:, :, 0] = grey
    result[:, :, 1] = grey
    result[:, :, 2] = grey
    _show(result, "Grey")
    return result
