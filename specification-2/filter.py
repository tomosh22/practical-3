from PIL import Image,ImageFilter


def filter(img):
    image = Image.open(img)
    filter = input("""
    Choose filter:
        b:Blur
        c:Contour
        d:Detail
    """)
    if filter == "b":
        image = image.filter(ImageFilter.BLUR)
    elif filter == "c":
        image = image.filter(ImageFilter.CONTOUR)
    elif filter == "d":
        image = image.filter(ImageFilter.DETAIL)
    new_name = "." + img.split(".")[1] + filter + ".jpg"
    print(new_name)
    image.save(new_name, "JPEG")
    image.show()
