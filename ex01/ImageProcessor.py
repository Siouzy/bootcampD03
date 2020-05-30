import matplotlib.pyplot as plt
import numpy as np


class ImageProcessor:

    def load(self, path):
        image = plt.imread(path)
        print('Loaded {:s} with dimensions {:d} * {:d}'.
              format(path, image.shape[0], image.shape[1]))
        return image

    def display(self, array):
        plt.imshow(array)
        plt.show()
