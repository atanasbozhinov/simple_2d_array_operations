import numpy as np

def append(input_x, input_y):
    output = np.append(input_x, input_y, axis=0)

    return output

def combine(input_x, input_y):
    output = np.append(input_x, input_y, axis=1)

    return output