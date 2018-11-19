import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-x_trn', required=True, help='Training Images Filepath')
ap.add_argument('-y_trn', required=True, help='Training Labels Filepath')
args = vars(ap.parse_args())

def build_model(input_shape: tuple, output_shape: int) -> Sequential:
    '''Function to define structure, build, and return a neural network model.'''

    model = Sequential()
    model.add(Conv2D(filters=32, kernel_size=(3,3), activation='relu', input_shape=input_shape))
    model.add(Conv2D(filters=64, kernel_size=(3,3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Flatten())
    model.add(Dropout(0.5))
    model.add(Dense(64, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(output_shape, activation='softmax'))

    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    return model

if __name__ == '__main__':

    # Dataset Shapes
    #   x_train.shape: (60000, 28, 28, 1)
    #   y_train.shape: (60000, 10)

    # load datasets
    x = np.load(args['x_trn'])
    y = np.load(args['y_trn'])

    # create model
    model = build_model((28,28,1), 10)

    # train model
    TH = model.fit(x, y, batch_size=128, epochs=15, validation_split=0.3, shuffle=True, verbose=1)

    # show results
    print("Done Training: ")
    print('Final Training Accuracy: ', TH.history['acc'][-1])
    print('Final Validation Accuracy: ', TH.history['val_acc'][-1])

    # save model
    model.save('./src/models/mnistCNN.h5')

    '''
    Current Model Training Statistics:
        Final Training Accuracy:  0.9840476190476191
        Final Validation Accuracy:  0.9884444444444445
    '''