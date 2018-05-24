import ImageGathering.image_handling as image_handler
import KerasClass.KerasClass as CustomKeras
import numpy as np

train_batches, train_labels = image_handler.get_train_data(root='KerasClass/Images/train')
test_batches, test_labels = image_handler.get_train_data(root='KerasClass/Images/validate')
obj = CustomKeras.cnn()
obj.train(train_batches, train_labels)

