import csv
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
from dotenv import load_dotenv
import os

load_dotenv('config.env')
# get config from env
batchsize = int(os.getenv('BATCH_SIZE'))
targetx = int(os.getenv('TARGET_X'))
targety = int(os.getenv('TARGET_Y'))

model = tf.keras.models.load_model('modelv1.h5')

fileNames = []
imageData = []

testDir = 'data/train/malignant'

total = len(os.listdir(testDir))
item = 1
for file in os.listdir(testDir):
    path = testDir + '/' + file
    img = image.load_img(path, target_size=(targetx, targety))
    x = image.img_to_array(img)
    #x = np.expand_dims(x, axis=0)
    print('{pct}% complete'.format(pct=round(100 * (item/total))))
    item += 1

    fileNames.append(file[:12])
    imageData.append(x)

imageData = np.array(imageData)
#print(fileNames.shape, imageData.shape)
preds = model.predict(imageData, batch_size=50)
preds = preds.tolist()

f = open('submission.csv', 'w')
f.write('image_name,target')
f.write('\n')
length = len(preds)

index = 0
for prediction in preds:
    print('{image_name},{target}'.format(image_name=fileNames[index], target=prediction[0]))
    print('{pct}% complete'.format(pct=round((index+1) / length * 100)))
    f.write('{image_name},{target}'.format(image_name=fileNames[index], target=prediction[0]))
    f.write('\n')
    index += 1
f.close()
