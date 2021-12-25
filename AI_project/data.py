import cv2 as cv
import numpy as np

labels = [
    'limit 5 km/h',
    'limit 15 km/h',
    'limit 30 km/h',
    'limit 40 km/h',
    'limit 50 km/h',
    'limit 60 km/h',
    'limit 70 km/h',
    'limit 80 km/h',
    'No proceed straight and left turns',
    'No proceed straight and right turns',
    'No proceed straight',
    'No left turn',
    'No left and right turns',
    'No right turn',
    'No overtaking',
    'No U-turns',
    'No motor vehicles',
    'No honking',
    'End of maximum speed limit 40km/h',
    'End of maximum speed limit 50km/h',
    'Proceed straight and/or Turn right',
    'One-way street',
    'Turn left',
    'Turn left and/or right',
    'Turn right',
    'Keep left side',
    'Keep right side',
    'Roundabout',
    'Limited-access road',
    'Honking',
    'Bicycles only',
    'Lane for U-turn',
    'Turn left and/or right to detour',
    'Traffic signals ahead',
    'Other danger',
    'Pedestrian crossing ahead',
    'Cyclists',
    'School ahead',
    'Curve to the right',
    'Curve to the left',
    'Steep descent',
    'Steep ascent',
    'Slow',
    'Side road junction ahead on the right',
    'Side road junction ahead on the left',
    'Cross-village road',
    'Double curve, with turn right first, then left',
    'Level crossing ahead (without safety barriers)',
    'Roadworks ahead',
    'Multiple curve',
    'Level crossing ahead (with safety barriers)',
    'Accident area',
    'Stop sign',
    'No entry for vehicular and pedestrians',
    'No stopping',
    'No entry for vehicular traffic',
    'Give way',
    'Control'
]

#lay du lieu train, test
def load_data():
    train_img = []
    train_label = []
    val_img = []
    val_label = []
    with open('train.txt', 'r') as f:
        for img in f.readlines():
            elm = img.split(';')
            img = cv.imread('train/' + elm[0])
            img = img[int(elm[4]): int(elm[6]), int(elm[3]): int(elm[5])]
            img = cv.resize(img, dsize=(120,120))
            train_img.append(img)
            train_label.append(int(elm[7]))
    with open('test.txt', 'r') as f:
        for img in f.readlines():
            elm = img.split(';')
            img = cv.imread('test/' + elm[0])
            img = img[int(elm[4]): int(elm[6]), int(elm[3]): int(elm[5])]
            img = cv.resize(img, dsize=(120,120))
            val_img.append(img)
            val_label.append(int(elm[7]))
    return (np.array(train_img, dtype=np.uint8), np.array(train_label, dtype=np.uint8)), (np.array(val_img,dtype=np.uint8), np.array(val_label, dtype=np.uint8))