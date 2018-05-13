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
    filenames = os.listdir(directory)
    filenames = [os.path.join(directory, filename) for filename in filenames]

    return [cv2.imread(filename) for filename in filenames]


def get_train_data(root="train_data"):
    """
    Gets all the logits and labels train data from directory
    :return: array of (logits, labels).T
    """
    foldernames = os.listdir(root)
    foldernames = [os.path.join(root, foldername) for foldername in foldernames]
    encoding = one_hot_encoding(len(foldernames))
    data = [get_images_from_path(directory) for directory in foldernames]
    return np.array([data, encoding]).T


def one_hot_encoding(num):
    """
    Generates an array of one hot encoding based off of a num value
    :param num: number of possible classifications
    :return: if num = 3, returns [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    """
    return [[0]*x + [1] + [0]*num-x-1 for x in range(num)]