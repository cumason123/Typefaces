import cv2, os
import numpy as np


def get_image_shape(filepath):
    """
    Gets the shape for a given image

    :param filepath  string indicating the local/absolute path for a given image
    :returns array indicating the given image shape
    """
    return np.shape(cv2.imread(filepath))


def get_images_from_path(directory):
    """
    Gets and returns np.array of all images inside of a given directory

    :param directory: directory name
    :return: np.array of images
    """
    # print(directory)
    filenames = os.listdir(directory)
    filenames = [os.path.join(directory, filename) for filename in filenames]
    # print(filenames)
    return [cv2.imread(filename) for filename in filenames]


def get_train_data(root="train_data"):
    """
    Gets all the logits and labels train data from directory

    :return: tuple where (logits, labels)
    """
    foldernames = os.listdir(root)
    foldernames = [os.path.join(root, foldername) for foldername in foldernames]
    # print(foldernames)
    encoding = one_hot_encoding(len(foldernames))
    data = []
    labels = []
    for directory in foldernames:
        subData = get_images_from_path(directory)
        data += subData
        print("Final Output: "+str(np.shape(data)))
    return np.array(data), np.array(labels)


def one_hot_encoding(num):
    """
    Generates an array of one hot encoding based off of a num value

    :param num: number of possible classifications
    :return: if num = 3, returns [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    """
    return np.array([[0]*x + [1] + [0]*(num-x-1) for x in range(num)])

if __name__ == "__main__":
    x, y = get_train_data(root="typefonts")
    print(x)
