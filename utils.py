from scipy import signal
import numpy as np

def create_2d_gaussian(size: float=9, std: float=1.5) -> np.ndarray:
    "Create a 2-D gaussian blur filter for a given mean and std."
    gaussian_1d = signal.windows.gaussian(size,std=std)
    gaussian_2d = np.outer(gaussian_1d, gaussian_1d)
    gaussian_2d = gaussian_2d / (gaussian_2d.sum())
    return gaussian_2d

def normalize_img(img: np.ndarray) -> np.ndarray:
    "Normalize an image's pixel values to [0, 1]."
    return (img - img.min()) / (img.max() - img.min())