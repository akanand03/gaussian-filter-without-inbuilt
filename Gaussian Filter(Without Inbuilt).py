import cv2
import numpy as np
image = cv2.imread('lena.jpg')
kernel_size = 5
sigma = 1.0
kernel = np.fromfunction(lambda x, y: (1/ (2 * np.pi * sigma ** 2)) * np.exp(-((x - (kernel_size - 1) / 2) ** 2 + (y - (kernel_size - 1) / 2) ** 2) / (2 * sigma ** 2)), (kernel_size, kernel_size))
kernel /= np.sum(kernel)
height, width, channels = image.shape
smoothed_image = np.copy(image)
half_kernel = kernel_size // 2
for i in range(half_kernel, height - half_kernel):
    for j in range(half_kernel, width - half_kernel):
        for c in range(channels):

            weighted_sum = np.sum(image[i - half_kernel:i + half_kernel + 1, j - half_kernel:j + half_kernel + 1, c] * kernel)
            smoothed_image[i, j, c] = weighted_sum
cv2.imshow('Original Image', image)
cv2.imshow('Smoothed Image (Gaussian Filter)', smoothed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
