
import numpy as np

def get_np_from_file(path):
    array = []

    with open(path, 'r') as file:
        data = file.read()

        rows = data.split('\n')
        for row in rows:
            cols = row.split(' ')
            array.append([str(col) for col in cols])

    return np.array(array)