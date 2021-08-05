from PIL import Image, ImageTk,  ImageDraw
import uuid

img = Image.open('afyon3.png').convert('RGB')
lines = []
with open('sa.txt') as f:
    lines = f.readlines()
print(lines)
print(int(lines[0].split(" ")[1]))

img.show()
for line in lines:   
    crop_rectangle = (int(line.split(" ")[0]), int(line.split(" ")[1]), int(line.split(" ")[2]), int(line.split(" ")[3]))
    cropped_im = img.crop(crop_rectangle)
    cropped_im.save("./parklar/"+str(uuid.uuid4())+".png")