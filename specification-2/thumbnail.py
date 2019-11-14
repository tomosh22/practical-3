from PIL import Image


def thumbnail(img):
    image = Image.open(img)

    # change size of image to 100x100 and apply antialiasing
    image = image.resize((100, 100), Image.ANTIALIAS)

    # determine where to save the altered image and alter the file name
    new_name = ".." + img[2:].split(".")[0] + "thumb" + ".jpg"

    # saves and displays new image
    image.save(new_name, "JPEG")
    image.show()
