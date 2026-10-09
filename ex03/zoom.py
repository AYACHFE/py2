import matplotlib.pyplot as plt
import numpy as np

from load_image import ft_load


def zoom(pixels: np.ndarray, top: int = 100, left: int = 450,
         size: int = 400) -> np.ndarray:
    """Crop a square region of the image and keep a single channel."""
    if pixels.ndim != 3:
        raise ValueError("image must have 3 dimensions")
    height, width = pixels.shape[:2]
    if top + size > height or left + size > width:
        raise ValueError(
            f"zoom area does not fit in the image ({height}x{width})"
        )
    cropped = pixels[top:top + size, left:left + size, 0:1]
    print(f"New shape after slicing: {cropped.shape}")
    return cropped


def main() -> None:
    """Load an image, zoom on it, print the data and display the result."""
    try:
        pixels = ft_load("animal.jpeg")
        print(pixels)
        cropped = zoom(pixels)
        print(cropped)

        plt.imshow(cropped, cmap="gray")
        plt.xlabel("X (pixels)")
        plt.ylabel("Y (pixels)")
        plt.show()
    except ValueError as problem:
        print(f"Error: {problem}")
    except Exception as problem:
        print(f"Unexpected error: {problem}")


if __name__ == "__main__":
    main()
