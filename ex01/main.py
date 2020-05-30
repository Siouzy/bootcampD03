from ImageProcessor import ImageProcessor
import numpy as np
import sys

img_path = sys.argv[1]
imgp = ImageProcessor()
img = imgp.load(img_path)
imgp.display(img)