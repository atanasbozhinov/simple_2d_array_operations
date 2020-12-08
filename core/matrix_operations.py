import numpy as np

def append(input_x, input_y):
    try:
        output = np.append(input_x, input_y, axis=0)
    except ValueError:
        return None

    return output

def combine(input_x, input_y):
    try:
        output = np.append(input_x, input_y, axis=1)
    except ValueError:
        return None

    return output

def sum(input_x, input_y):
    if not (input_x.shape == input_y.shape):
        return None

    output = np.add(input_x, input_y)

    return output