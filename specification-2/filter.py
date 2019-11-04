from PIL import Image,ImageFilter


def filter(img):
    image = Image.open(img)
    filter = input("""
    Choose filter:
        b:Blur
        c:Contour
        d:Detail
        e:Edge Enhance
        e+:Edge Enhance More
        em:Emboss
        f:Find Edges
        s:Sharpen
        sm:Smooth
        sm+:Smooth More
    """)
    if filter == "b":
        image = image.filter(ImageFilter.BLUR)
    elif filter == "c":
        image = image.filter(ImageFilter.CONTOUR)
    elif filter == "d":
        image = image.filter(ImageFilter.DETAIL)
    elif filter == "e":
        image = image.filter(ImageFilter.EDGE_ENHANCE)
    elif filter == "e+":
        image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
    elif filter == "em":
        image = image.filter(ImageFilter.EMBOSS)
    elif filter == "f":
        image = image.filter(ImageFilter.FIND_EDGES)
    elif filter == "s":
        image = image.filter(ImageFilter.SHARPEN)
    elif filter == "sm":
        image = image.filter(ImageFilter.SMOOTH)
    elif filter == "sm+":
        image = image.filter(ImageFilter.SMOOTH_MORE)
    new_name = "." + img.split(".")[1] + filter + ".jpg"
    print(new_name)
    image.save(new_name, "JPEG")
    image.show()
