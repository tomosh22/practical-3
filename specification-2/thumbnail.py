from PIL import Image
def thumbnail(img):
    print(img)
    image = Image.open(img)
    image = image.resize((100,100), Image.ANTIALIAS)
    new_name = "." + img.split(".")[1] + "thumb.jpg"
    print(new_name)
    image.save(new_name, "JPEG")
    image.show()