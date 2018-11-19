import sys
import unittest
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model

class ShapeTesting(unittest.TestCase):
    def setUp(self):
        self.model = load_model('./src/models/mnistCNN.h5')

    def test_InputShape(self):
        layer0 = self.model.layers[0]
        input_shape = layer0.input.shape
        input_shape_tuple = []
        for i in range(len(input_shape)):
            input_shape_tuple.append(input_shape[i].value)
        input_shape_tuple = tuple(input_shape_tuple)
        self.assertEqual(input_shape_tuple, (None, 28, 28, 1))

class AccuracyTesting(unittest.TestCase):
    def setUp(self):
        self.model = load_model('./src/models/mnistCNN.h5')

    def test_Accuracy(self):
        x = np.load('./datasets/TestData/x_test.npy')
        y = np.load('./datasets/TestData/y_test.npy')
        score = self.model.evaluate(x, y, verbose=0)
        acc = score[1]
        self.assertTrue(acc >= .97)

if __name__ == '__main__':
    unittest.main()
