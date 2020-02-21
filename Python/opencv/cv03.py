import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('img2.png',1)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y axis
plt.show()