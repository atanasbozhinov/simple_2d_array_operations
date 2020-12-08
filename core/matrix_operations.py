import numpy as np

def append(input_x, input_y):
    output = np.append(input_x, input_y, axis=0)

    return output

def combine(input_x, input_y):
    output = np.append(input_x, input_y, axis=1)

    return output

def sum(input_x, input_y):
    output = np.add(input_x, input_y)

    return output