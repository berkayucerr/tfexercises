import cv2
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
Categories=['Cat','Dog']
def prepare(filepath):
    IMG_SIZE = 50
    img_array = cv2.imread(filepath,cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    return np.array(new_array).reshape(-1,IMG_SIZE,IMG_SIZE,1)


model = tf.keras.models.load_model('64x3-CNN.model')
predictions = model.predict([prepare("dog.jpg")])
print(Categories[int(predictions[0][0])])

