from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Dense, Flatten
from keras.models import Sequential
from keras.models import load_model
from keras.optimizers import adam
from keras.preprocessing.image import ImageDataGenerator
from keras.layers.convolutional import *


train_path = 'Images/train'
test_path = 'Images/test'
validate_path = 'Images/validate'

train_batches = ImageDataGenerator().flow_from_directory(train_path, target_size=(100, 100), classes=['Andale', 'Arial', 'Georgia'], batch_size=7)
validate_batches = ImageDataGenerator().flow_from_directory(validate_path, target_size=(100, 100), classes=['Andale', 'Arial', 'Georgia'], batch_size=3)
test_batches = ImageDataGenerator().flow_from_directory(test_path, target_size=(100, 100), classes=['Andale', 'Arial', 'Georgia'], batch_size=10)


batch_size = 32
epochs = 30

class cnn:

    def __init__(self, input_dim):
        model = Sequential()
        model.add(Conv2D(32, kernel_size=(3, 3), strides=(1, 1), padding='same',
                         input_shape=(100, 100, 3),
                         activation='relu'))
        model.add(Conv2D(64, (5, 5), activation='relu'))
        model.add(MaxPooling2D())
        model.add(Conv2D(64, (5, 5), activation='relu'))
        model.add(Flatten())
        model.add(Dense(256, kernel_initalizer='uniform', activation='relu'))
        model.add(Dense(3, kernel_initalizer='uniform', activation='softmax'))

        self.cnn = model

        model.compile(loss='categorical_crossentropy', optimizer=adam, metrics=['accuracy'])
        model.fit(train_batches, steps_per_epoch=4, validation_data=validate_batches, validation_steps=4, epochs=5,
                  verbose=20)












def save_model(self):
    self.model.save('model.h5')



def load_model(self):
    self.model = load_model('model.h5')




