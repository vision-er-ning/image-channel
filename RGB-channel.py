from PIL import Image
img = Image.open('F:/python/image-channel/408.jpg')
print(img.mode)
if img.mode == "P":
   img = img.convert('RGB')
img.save('F:/python/image-channel')#img.save('C:/Users/lenovo/Desktop/新建文件夹 (3)/save.png')


