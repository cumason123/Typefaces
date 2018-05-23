from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Dense, Flatten
from keras.models import Sequential
from keras.models import load_model
from keras.optimizers import SGD
from keras.callbacks import LearningRateScheduler, ModelCheckpoint



class cnn:

    def __init__(self, input_dim):
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

        lr = 0.01
        sgd = SGD(lr=lr, decay=1e-6, momentum=0.9, nesterov=True)
        model.compile(loss='categorical_crossentropy',
                      optimizer=sgd,
                      metrics=['accuracy'])


def learn_rate(epoch):
    return lr * (0.1 ** int(epoch / 10))

batch_size = 32
epochs = 30

model.fit(X, Y,
        batch_size=batch_size,
        epochs=epochs,
        validation_split=0.2,
        callbacks=[LearningRateScheduler(lr_schedule),
                    ModelCheckpoint('model.h5', save_best_only=True)]
        )


    def save_model(self):
        self.model.save('model.h5')



    def load_model(self):
        self.model = load_model('model.h5')  # type: object



