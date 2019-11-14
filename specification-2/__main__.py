from os import listdir
from filter import filter
from thumbnail import thumbnail

if __name__ == "__main__":
    # append all images in provided img directory to images array
    images = []
    for img in listdir("../resources/img/spec2-images"):
        images.append("../resources/img/spec2-images/"+img)

    # obtain user input to determine which function to call
    choice = input("""
        t:Thumbnail
        f:Filter
    """)

    if choice == "t":
        func = thumbnail
    elif choice == "f":
        func = filter

    # display all images in images array and obtain user input to determine which image to alter
    for x in range(len(listdir("../resources/img/spec2-images"))):
        print(str(x)+":"+images[x])
    img_choice = int(input("Which image index?"))
    func(images[img_choice])

