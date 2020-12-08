
import unittest
import numpy as np
import core.input as inp


class InputTests(unittest.TestCase):
    def test_table_format(self):
        input_x_path = "samples/table_format1"
        input_y_path = "samples/table_format2"
        expected_output_x = np.array([[1, 2, 3], [4, 5, 6]])
        expected_output_y = np.array([[7, 8, 9], [10, 11, 12], [13, 14, 15]])

        output_x = inp.get_np_from_file(input_x_path)
        output_y = inp.get_np_from_file(input_y_path)

        self.assertTrue(np.array_equal(expected_output_x, output_x))
        self.assertTrue(np.array_equal(expected_output_y, output_y))

if __name__ == '__main__':
    unittest.main()