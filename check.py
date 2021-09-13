from PIL import Image, ImageTk,  ImageDraw,ImageOps
import uuid
import os, shutil
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import tensorflow.keras
import numpy as np
from selenium import webdriver
import time

driver = webdriver.Chrome('C:/Users/onurs/Desktop/chromedriver.exe')
driver.get('http://seyret.nigde.bel.tr/')

time.sleep(2)
el=driver.find_element_by_xpath('//*[@id="tab1"]')


el.click()
time.sleep(0.1)
el.click()
time.sleep(2)

driver.save_screenshot("shot.png")
driver.quit()
ss = Image.open("shot.png")


target='shot.png'
# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = tensorflow.keras.models.load_model('keras_model.h5',compile=False)

data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

def isOccupied(filename):
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
        return True
    else:
        return False

fig, ax = plt.subplots()
im = Image.open(target)
ax.imshow(im)
img = Image.open(target).convert('RGB')
lines = []
with open('sa.txt') as f:
    lines = f.readlines()
print(lines)
print(int(lines[0].split(" ")[1]))


directory = './parklar'
for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))


for line in lines:   
    crop_rectangle = (int(line.split(" ")[0]), int(line.split(" ")[1]), int(line.split(" ")[2]), int(line.split(" ")[3]))
    cropped_im = img.crop(crop_rectangle)
    temp_id = str(uuid.uuid4())
    cropped_im.save("./parklar/"+temp_id+".png")
    occupied=isOccupied(temp_id+".png")
    print(occupied)
    if occupied:
        color="r"
    else:
        color="g"
    ax.add_patch(Rectangle((int(line.split(" ")[0]), int(line.split(" ")[1])), int(line.split(" ")[2])-int(line.split(" ")[0]), int(line.split(" ")[3])-int(line.split(" ")[1]),linewidth=1, edgecolor=color, facecolor='none'))



#display plot
plt.savefig('foo.png')
plotimage = Image.open('foo.png').convert('RGB')
plotimage.show()


