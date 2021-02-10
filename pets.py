import matplotlib.pyplot as plt
import cv2
import os
import numpy as np

DATADIR = "/Users/berkayucer/Downloads/kagglecatsanddogs_3367a/PetImages"
CATEGORIES = ["Dog","Cat"]
IMG_SIZE=50
TRAINING_DATAS=[]
def create_training_data():
    for category in CATEGORIES:
        path = os.path.join(DATADIR, category)
        class_num = CATEGORIES.index(category)
        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
                new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
                TRAINING_DATAS.append([new_array,class_num])
            except Exception as e:
                pass

create_training_data()
print(len(TRAINING_DATAS))
import random
random.shuffle(TRAINING_DATAS)
for sample in TRAINING_DATAS[:10]:
    print(sample[1])

X=[]
Y=[]
for features,labels in TRAINING_DATAS:
    X.append(features)
    Y.append(labels)
X=np.array(X).reshape(-1,IMG_SIZE,IMG_SIZE,1)
import pickle
pickle_out_X=open('X.pickle','wb')
pickle_out_Y=open('Y.pickle','wb')
pickle.dump(X,pickle_out_X)
pickle.dump(Y,pickle_out_Y)
pickle_out_X.close()
pickle_out_Y.close()
