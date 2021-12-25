import keras.losses
import data
from keras import Sequential
from keras.layers import Conv2D, Dense, MaxPool2D, Flatten

(train_img,train_label), (val_img, val_label) = data.load_data()

model = Sequential()
model.add(Conv2D(64,kernel_size=(3,3), activation='sigmoid', input_shape=(120,120,3)))
model.add(Conv2D(64,kernel_size=(3,3), activation='relu'))
model.add(MaxPool2D(pool_size=(2,2)))
model.add(Conv2D(128,kernel_size=(3,3), activation='relu'))
model.add(MaxPool2D(pool_size=(2,2)))
model.add(Conv2D(128,kernel_size=(3,3), activation='relu'))
model.add(MaxPool2D(pool_size=(2,2)))
model.add(Conv2D(128,kernel_size=(3,3), activation='relu'))
model.add(MaxPool2D(pool_size=(2,2)))
model.add(Flatten())
model.add(Dense(512, activation='relu'))
model.add(Dense(58, activation='softmax'))
model.compile(optimizer='adam', loss=keras.losses.sparse_categorical_crossentropy, metrics=['accuracy'])
model.summary()

model.fit(train_img, train_label,validation_data=(val_img, val_label), epochs=5)
model.save('traffic_sign_model')