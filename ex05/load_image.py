import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """
    Load an image from disk and return its pixel data.

    Parameters:
        path (str): location of the image file to load.

    Returns:
        np.ndarray: array representation of the image.
    """
    try:
        with Image.open(path) as img:
            pixels = np.asarray(img).copy()
    except Exception as e:
        exit(f'Exception: {e}')

    print(f"The shape of the image is: {pixels.shape}")
    print(pixels)
    return pixels
