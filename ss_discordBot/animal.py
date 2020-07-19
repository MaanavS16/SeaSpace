from tensorflow.keras import backend as K
from tensorflow.keras.applications.vgg16 import VGG16
import numpy as np
from tensorflow.keras.applications.vgg16 import decode_predictions
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import preprocess_input
import pandas as pd
from PIL import Image
import requests
from io import BytesIO


K.clear_session()


class Predictor:
    def __init__(self, modelWeights='imagenet'):
        self.model = VGG16(weights='imagenet')

    def predictPic(self, url):
        # load and resize image
        resp = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        im = Image.open(BytesIO(resp.content))
        im = im.resize((224, 224))

        if im.mode != 'RGB':
            im = im.convert('RGB')

        #Convert Image to Numpy Array
        x = image.img_to_array(im)
        x = np.expand_dims(x, axis=0)
        print(x.shape)
        #Place image into outer-array layer (Required by model)


        #Pre-process
        x = preprocess_input(x)
        preds = self.model.predict(x)
        predictions = pd.DataFrame(decode_predictions(preds, top=3)[0],columns=['col1','category','probability']).iloc[:,1:]
        #print('predicted class:', predictions.loc[0,'category'])
        return predictions.loc[0,'category']

#predictor = Predictor()
