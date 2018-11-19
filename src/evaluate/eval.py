import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-x_tst', required=True, help='Testing Images Filepath')
ap.add_argument('-y_tst', required=True, help='Testing Labels Filepath')
args = vars(ap.parse_args())

if __name__ == '__main__':

    # load datasets
    x = np.load(args['x_tst'])
    y = np.load(args['y_tst'])

    # load model
    model = load_model('./src/models/mnistCNN.h5')

    # evaluate model
    score = model.evaluate(x, y, verbose=1)

    # show results
    print("Done Testing: ")
    print('Final Testing Accuracy: ', score[1])

    '''
    Current Model Testing Statistics:
        Final Testing Accuracy:  0.9919
    '''