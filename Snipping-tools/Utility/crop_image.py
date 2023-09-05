import numpy as np
import cv2  # Assuming you're using OpenCV for image processing


def crop_image(image: np.ndarray, x: int, y: int, width: int, height: int):
    """
    Crop a region from an image and return it as a bytes object.

    Args:
        image (numpy.ndarray): The input image represented as a NumPy ndarray.
        x (int): The x-coordinate of the top-left corner of the crop.
        y (int): The y-coordinate of the top-left corner of the crop.
        width (int): The width of the crop.
        height (int): The height of the crop.

    Returns:
        bytes: The cropped region as a bytes object.

    Note:
        - This function assumes you are using OpenCV (cv2) for image processing.
        - The cropped region is flipped vertically before converting to bytes.
          You may want to adjust this behavior based on your requirements.
    """
    # Crop the region and flip it vertically (you can adjust this behavior)
    cropped_array = image[int(y):int(y + height), int(x):int(x + width)]
    # cropped_image = cv2.flip(cropped_array, 0).tobytes()
    return cropped_array.tobytes()
