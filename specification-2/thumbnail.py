from PIL import Image
def thumbnail(img):
    print(img)
    image = Image.open(img)
    image = image.resize((100,100), Image.ANTIALIAS)
    new_name = ".." + img[2:].split(".")[0] + filter + ".jpg"
    image.save(new_name, "JPEG")
    image.show()
