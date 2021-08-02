from PIL import Image, ImageTk,  ImageDraw
import uuid

img = Image.open('DENEME_BOSS.png').convert('RGB')
lines = []
with open('sa.txt') as f:
    lines = f.readlines()
print(lines)
print(int(lines[0].split(" ")[1]))
img1 = ImageDraw.Draw(img)  
img1.rectangle([(int(lines[0].split(" ")[0]), int(lines[0].split(" ")[1])), (int(lines[0].split(" ")[2]), int(lines[0].split(" ")[3]))],  outline ="red",width=5)
img.show()
for line in lines:   
    crop_rectangle = (int(line.split(" ")[0]), int(line.split(" ")[1]), int(line.split(" ")[2]), int(line.split(" ")[3]))
    cropped_im = img.crop(crop_rectangle)
    cropped_im.save("./parklar/"+str(uuid.uuid4())+".png")