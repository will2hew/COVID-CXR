import os

import tensorflow as tf

k = tf.keras

def simple_covid_net():

    covid_net = k.models.Sequential()

    ##################################
    #  FIRST EXPERIMENT - Basic CNN  #
    ##################################

    covid_net.add(k.layers.Conv2D(32, kernel_size=(3,3), activation='relu', input_shape=(224,224,1)))
    covid_net.add(k.layers.Conv2D(64, kernel_size=(3,3), activation='relu'))
    covid_net.add(k.layers.MaxPooling2D(pool_size=(2,2)))
    covid_net.add(k.layers.Dropout(0.25))
    covid_net.add(k.layers.Flatten())
    covid_net.add(k.layers.Dense(128, activation='relu'))
    covid_net.add(k.layers.Dropout(0.5))
    covid_net.add(k.layers.Dense(3, activation='softmax'))

    return covid_net