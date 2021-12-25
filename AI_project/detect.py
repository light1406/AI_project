import cv2 as cv
import keras.models
import numpy as np
from data import labels

def classificate(img):
    model = keras.models.load_model('traffic_sign_model')
    cascade = cv.CascadeClassifier('cascade1/cascade.xml')
    traffic = cascade.detectMultiScale(img)
    for (x,y,w,h) in traffic:
        img1 = img[y: y + h, x: x + w]
        img1 = cv.resize(img1, dsize=(120,120))
        result = model.predict(np.array([img1]))
        label = labels[np.argmax(result)]
        scale = round((np.max(result) * 100), 2)
        clf = label + " : " + str(scale) + '%'
        print(clf)
        img = cv.rectangle(img, (x,y), (x + w,y+h), (255,0,0),thickness=1)
        img = cv.putText(img,clf,org=(x, y - 1), fontFace=cv.FONT_HERSHEY_SIMPLEX, fontScale=0.7, color=(255,0,0), thickness=2)
    print('==========================')
    return cv.cvtColor(img, cv.COLOR_BGR2RGBA)