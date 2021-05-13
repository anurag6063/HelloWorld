#!/usr/bin/env python
# coding: utf-8

#     import required packages

# In[1]:



from keras.models import Sequential

from keras.layers import Flatten,Dense,MaxPooling2D,Conv2D

# initialize the CNN

classifier = Sequential()
# creted an object of sequential the dhancha of NN

classifier.add(Conv2D(32, (3,3), input_shape = (64,64,3), activation='relu'))

classifier.add(MaxPooling2D(pool_size= (2,2)))

classifier.add(Conv2D(32,(3,3), activation='relu'))

classifier.add(MaxPooling2D(pool_size=(2,2)))

classifier.add(Flatten())

classifier.add(Dense(units=128, activation='relu'))

classifier.add(Dense(units=1, activation='sigmoid'))

classifier.compile(loss='binary_crossentropy',  optimizer='adam', metrics=['accuracy'])

from keras_preprocessing.image import ImageDataGenerator

train_datagen=ImageDataGenerator(
    rescale=1./255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True
)

test_datagen = ImageDataGenerator(rescale = 1./255)

training_set =train_datagen.flow_from_directory(

    '/home/aprayo/anaconda3/jupyter_code_base/data/Convolutional_Neural_Networks/dataset/training_set',
    target_size=(64,64),
    batch_size=32,
    class_mode='binary'
)

test_set =test_datagen.flow_from_directory('/home/aprayo/anaconda3/jupyter_code_base/data/Convolutional_Neural_Networks/dataset/test_set',
                                target_size=(64,64),
                                batch_size=32,
                                class_mode='binary')

classifier.fit_generator(
    training_set,
    steps_per_epoch=8000,
    epochs=25,
    validation_data=test_set,
    validation_steps=2000

)

classifier.save('./classifier',overwrite=True, include_optimizer=True)

get_ipython().system('pwd')

import numpy as np
from keras.preprocessing import image
test_image = image.load_img('/home/aprayo/anaconda3/jupyter_code_base/data/Convolutional_Neural_Networks/dataset/single_prediction/cat_or_dog_2.jpg', target_size = (64, 64))

test_image

test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result = classifier.predict(test_image)
training_set.class_indices

if result[0][0] == 1:
    prediction = 'dog'
    print('dog')
else:
    prediction = 'cat'
    print('cat')

