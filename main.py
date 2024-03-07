from PIL import Image
from matplotlib import pyplot as plt
from collections import Counter
from scipy import ndimage as ndi
from skimage import feature
import scipy.misc
import numpy as np
import statistics
import random
import scipy
import time
import matplotlib.pyplot as plt
import cv2
import numpy as np


def open_img(img):
    route = ("C:/Users/Alienware/Downloads/" + img)
    img = Image.open(route)
    img.show()


open_img("daniel.png")
