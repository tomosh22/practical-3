from os import listdir
from filter import filter
from thumbnail import thumbnail

if __name__ ==  "__main__":
    images = []
    for img in listdir("../resources/img/spec2-images"):
        images.append("../resources/img/spec2-images/"+img)
    choice = input("""
        t:Thumbnail
        f:Filter
    """)
    if choice == "t":
        func = thumbnail
    elif choice == "f":
        func = filter
    for x in range(len(listdir("../resources/img/spec2-images"))):
        print(str(x)+":"+images[x])
    img_choice = int(input("Which image index?"))
    func(images[img_choice])

