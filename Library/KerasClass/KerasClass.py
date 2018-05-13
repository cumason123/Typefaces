from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Dense, Flatten
from keras.models import Sequential
from keras.models import load_model


class CNN:

    def __init__(self):
        model = Sequential()
        model.add(Conv2D(32, kernel_size=(5, 5), strides=(1, 1),
                         activation='relu', input_shape=input_dim))
        model.add(Conv2D(64, (5, 5), activation='relu'))
        model.add(MaxPooling2D())
        model.add(Conv2D(64, (5, 5), activation='relu'))
        model.add(Flatten())
        model.add(Dense(256, kernel_initalizer='uniform', activation='relu'))
        model.add(Dense(3, kernel_initalizer='uniform', activation='relu'))


        self.cnn = model

    def save_model(self):
        model.save('model.h5')



    def load_model(self):
        new_model = load_model('model.h5')  # type: object


