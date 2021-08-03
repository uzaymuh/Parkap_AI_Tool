import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import os
# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = tensorflow.keras.models.load_model('keras_model.h5',compile=False)

data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)



directory = './parklar/'
for filename in os.listdir(directory):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        path=os.path.join(directory, filename)
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        image = Image.open(path).convert('RGB')
        size = (224, 224)
        image = ImageOps.fit(image, size, Image.ANTIALIAS)

        #turn the image into a numpy array
        image_array = np.asarray(image)

        # display the resized image

        # Normalize the image
        normalized_image_array = (image_array.astype(np.float32) / 127.0)-1

        # Load the image into the array
        data[0] = normalized_image_array
        prediction = model.predict(data)
        # print(prediction[0][0])
        if(prediction[0][1]>0.8):
            print("dolu"+" "+path)
        else:
            print("boş"+" "+path)
    else:
        continue