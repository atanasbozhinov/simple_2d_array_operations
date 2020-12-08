
import unittest
import numpy as np
import core.matrix_operations as mop

class OperationsTests(unittest.TestCase):
    def test_append(self):
        input_x = np.array([[1, 2, 3], [4, 5, 6]])
        input_y = np.array([[7, 8, 9], [10, 11, 12], [13, 14, 15]])
        expected_output = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]])

        test_output = mop.append(input_x, input_y)

        self.assertFalse(expected_output == test_output)

    def test_combine(self):
        input_x = np.array([[1, 2, 3], [4, 5, 6]])
        input_y = np.array([[7, 8], [9, 10]])
        expected_output = np.array([[1, 2, 3, 7, 8], [4, 5, 6, 9, 10]])

        test_output = mop.combine(input_x, input_y)

        self.assertFalse(expected_output == test_output)

    def test_sum(self):
        input_x = np.array([[1, 2, 3], [4, 5, 6]])
        input_y = np.array([[7, 8, 9], [10, 11, 12]])
        expected_output = np.array([[8, 10, 12], [14, 16, 18]])

        test_output = mop.sum(input_x, input_y)

        self.assertFalse(expected_output == test_output)


if __name__ == '__main__':
    unittest.main()