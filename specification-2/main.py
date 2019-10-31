from os import listdir
from thumbnail import thumbnail
from filter import filter
if __name__ ==  "__main__":
    images = []
    for img in listdir("./img"):
        images.append("./img/"+img)
    filter(images[1])