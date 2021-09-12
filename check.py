from PIL import Image, ImageTk,  ImageDraw
import uuid
import os, shutil

img = Image.open('sampuan5.png').convert('RGB')
lines = []
with open('sa.txt') as f:
    lines = f.readlines()
print(lines)
print(int(lines[0].split(" ")[1]))


folder = './parklar'
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
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
    cropped_im.save("./parklar/"+str(uuid.uuid4())+".png")