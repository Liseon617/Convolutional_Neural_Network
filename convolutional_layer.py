import sys
print(sys.executable)

import numpy as np
from layer import Layer
from scipy import signal

#
class Convolutional(Layer):
    def __init__(self, input_shape, kernal_size, depth):
        input_depth, input_height, input_width = input