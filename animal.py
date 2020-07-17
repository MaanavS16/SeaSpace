import tensorflow as tf
from tensorflow.keras import backend as K
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from skimage import io
from tensorflow.keras.applications.vgg16 import VGG16
import numpy as np
from keras.applications.vgg16 import decode_predictions
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
import pandas as pd

K.clear_session()

blnUploadImage = False

model = VGG16(weights='imagenet')
class Predictor:

    def predictPic(path):
        #Resize Image
        img = image.load_img(path, target_size=(224, 224))

        #Convert Image to Numpy Array
        x = image.img_to_array(img)

        #Place image into outer-array layer (Rquired by model)
        import numpy as np
        x = np.expand_dims(x, axis=0)

        #Pre-process
        x = preprocess_input(x)
        preds = model.predict(x)
        predictions = pd.DataFrame(decode_predictions(preds, top=3)[0],columns=['col1','category','probability']).iloc[:,1:]
        print('predicted class:', predictions.loc[0,'category'])

predictor = Predictor()
