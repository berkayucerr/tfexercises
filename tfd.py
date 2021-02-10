import matplotlib.pyplot as plt
import tensorflow as tf

(x_train,y_train),(x_test,y_test)=tf.keras.datasets.imdb.load_data()

print(x_train.shape)
model=tf.keras.Sequential()
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(300,activation='relu'))
model.add(tf.keras.layers.Dense(128,activation='relu'))
model.add(tf.keras.layers.Dense(300,activation='relu'))
model.add(tf.keras.layers.Dense(1,activation='softmax'))
model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
model.fit(x_train,y_train,epochs=5,batch_size=1)
model.evaluate(x_test,y_test)
