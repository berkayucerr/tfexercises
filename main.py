from tensorflow.keras.layers import Dense,Flatten,Dropout,Activation,Conv2D,MaxPooling2D
from tensorflow.keras.models import Sequential
import tensorflow as tf
import numpy as np
import pickle
import cv2
from tensorflow.python.compiler.mlcompute import mlcompute
mlcompute.set_mlc_device(device_name='cpu')
Categories = ['Cat','Dog']
X = pickle.load(open('X.pickle','rb'))
y = pickle.load(open('Y.pickle','rb'))
X = np.array((X/255.0))
y = np.array((y))

model = Sequential()
model.add(Conv2D(64,(3,3),input_shape=X.shape[1:]))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(64,(3,3)))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Flatten())
model.add(Dense(64))

model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss="binary_crossentropy",metrics=['accuracy'],optimizer="adam")
model.fit(X,y,batch_size=100,epochs=10,validation_split=0.3)

def prepare(filepath):
    IMG_SIZE = 50
    img_array = cv2.imread(filepath,cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    return np.array(new_array).reshape(-1,IMG_SIZE,IMG_SIZE,1)

predictions = model.predict([prepare("kedi.jpg")])
pred2=model.predict([prepare('kopek.jpg')])
print(Categories[int(predictions[0][0])])
print(Categories[int(pred2[0][0])])
