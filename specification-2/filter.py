from PIL import Image, ImageFilter


def get_pixel(image, i, j):
  # Inside image bounds?
  width, height = image.size
  if i > width or j > height:
    return None

  # Get Pixel
  pixel = image.getpixel((i, j))
  return pixel


def convert_primary(image):
  # Get size
  image = Image.open(image)
  width, height = image.size

  # Create new Image and a Pixel Map
  #image = Image.open(image)
  pixels = image.load()

  # Transform to primary
  for i in range(width):
    for j in range(height):
      # Get Pixel
      pixel = get_pixel(image, i, j)

      # Get R, G, B values (This are int from 0 to 255)
      red =  pixel[0]
      green = pixel[1]
      blue = pixel[2]

      # Transform to primary
      if red > 127:
        red = 255
      else:
        red = 0
      if green > 127:
        green = 255
      else:
        green = 0
      if blue > 127:
        blue = 255
      else:
        blue = 0

      # Set Pixel in new image
      pixels[i, j] = (int(red), int(green), int(blue))

  # Return new image
  return image

# Create a Grayscale version of the image
def convert_grayscale(image):
  # Get size
  image = Image.open(image)
  width, height = image.size

  # Create new Image and a Pixel Map
  #new = create_image(width, height)
  pixels = image.load()

  # Transform to grayscale
  for i in range(width):
    for j in range(height):
      # Get Pixel
      pixel = get_pixel(image, i, j)

      # Get R, G, B values (This are int from 0 to 255)
      red =   pixel[0]
      green = pixel[1]
      blue =  pixel[2]

      # Transform to grayscale
      gray = (red * 0.299) + (green * 0.587) + (blue * 0.114)

      # Set Pixel in new image
      pixels[i, j] = (int(gray), int(gray), int(gray))

  # Return new image
  return image

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
        g:greyscale
        p:primary
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
    elif filter == "g":
        image = Image.open(img).convert('L')
    elif filter == "p":
        image = convert_primary(img)
    new_name = ".." + img[2:].split(".")[0] + filter + ".jpg"
    print(new_name)
    image.save(new_name, "JPEG")
    image.show()

