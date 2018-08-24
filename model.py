# -*- coding: utf-8 -*-
import logging

import tflearn
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression

from config import my_logger_name, tensorboard_verbose, checkpoint_path, best_checkpoint_path, max_checkpoints, \
    best_val_accuracy

my_logger = logging.getLogger(my_logger_name)


def createModel(nbClasses,imageSize):
    my_logger.debug("[+] Creating model...")
    convnet = input_data(shape=[None, imageSize, imageSize, 1], name='input')

    convnet = conv_2d(convnet, 64, 2, activation='elu', weights_init="Xavier")
    convnet = max_pool_2d(convnet, 2)

    convnet = conv_2d(convnet, 128, 2, activation='elu', weights_init="Xavier")
    convnet = max_pool_2d(convnet, 2)

    convnet = conv_2d(convnet, 256, 2, activation='elu', weights_init="Xavier")
    convnet = max_pool_2d(convnet, 2)

    convnet = conv_2d(convnet, 512, 2, activation='elu', weights_init="Xavier")
    convnet = max_pool_2d(convnet, 2)

    convnet = fully_connected(convnet, 1024, activation='elu')
    convnet = dropout(convnet, 0.5)

    convnet = fully_connected(convnet, nbClasses, activation='softmax')
    convnet = regression(convnet, optimizer='rmsprop', loss='categorical_crossentropy')

    model = tflearn.DNN(convnet, tensorboard_verbose=tensorboard_verbose,
                        checkpoint_path=checkpoint_path,
                        best_checkpoint_path=best_checkpoint_path,
                        max_checkpoints=max_checkpoints,
                        best_val_accuracy=best_val_accuracy)
    my_logger.debug("    Model created! ✅")
    return model
