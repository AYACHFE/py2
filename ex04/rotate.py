import matplotlib.pyplot as plt
import numpy as np

from load_image import ft_load


def crop_square(img: np.ndarray, size: int = 400,
                top: int = 100, left: int = 450) -> np.ndarray:
    """Cut a square region from the image and keep a single channel."""
    height, width = img.shape[:2]
    if top + size > height or left + size > width:
        raise ValueError(
            f"crop region ({size}x{size} at row {top}, col {left}) "
            f"does not fit in image of size {height}x{width}"
        )

    cropped = img[top:top + size, left:left + size]

    if cropped.ndim == 3:
        return cropped.mean(axis=2, keepdims=True).astype(np.uint8)
    return cropped[..., np.newaxis]


def transpose(matrix: np.ndarray) -> np.ndarray:
    """Transpose a 2D array manually: result[j][i] = matrix[i][j]."""
    rows, cols = matrix.shape
    result = np.zeros((cols, rows), dtype=matrix.dtype)
    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]
    return result


def main() -> None:
    try:
        img = ft_load("animal.jpeg")

        square = crop_square(img)
        print(f"The shape of image is: {square.shape} "
              f"or {square.shape[:2]}")
        print(square)

        flipped = transpose(square[:, :, 0])
        print(f"New shape after Transpose: {flipped.shape}")
        print(flipped)

        plt.imshow(flipped, cmap="gray")
        plt.xlabel("X (pixels)")
        plt.ylabel("Y (pixels)")
        plt.title("Transposed image")
        plt.show()

    except Exception as e:
        exit(f'Exception: {e}')


if __name__ == "__main__":
    main()
