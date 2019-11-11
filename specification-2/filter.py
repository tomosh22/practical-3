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
        g:greyscale
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
        img = Image.open('THEIMAGEGOESHERE').convert('LA')
        img.save('greyscale.png')
    elif filter == "primary":
#        new = convert_primary(original)
#           save_image(new, 'NEWIMAGE')
    new_name = "." + img.split(".")[1] + filter + ".jpg"
    print(new_name)
    image.save(new_name, "JPEG")
    image.show()

# # Imported PIL Library from PIL import Image
#
# # Open an Image
# def open_image(path):
#   newImage = Image.open(path)
#   return newImage
#
# # Save Image
# def save_image(image, path):
#   image.save(path, 'png')
#
#
# Create a new image with the given size
def create_image(i, j):
  image = Image.new("RGB", (i, j), "white")
  return image


# Get the pixel from the given image
def get_pixel(image, i, j):
  # Inside image bounds?
  width, height = image.size
  if i > width or j > height:
    return None

  # Get Pixel
  pixel = image.getpixel((i, j))
  return pixel

# Create a Primary Colors version of the image
def convert_primary(image):
  # Get size
  width, height = image.size

  # Create new Image and a Pixel Map
  new = create_image(width, height)
  pixels = new.load()

  # Transform to primary
  for i in range(width):
    for j in range(height):
      # Get Pixel
      pixel = get_pixel(image, i, j)

      # Get R, G, B values (This are int from 0 to 255)
      red =   pixel[0]
      green = pixel[1]
      blue =  pixel[2]

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
  return new
#
#
# # Main
# if __name__ == "__main__":
#   # Load Image (JPEG/JPG needs libjpeg to load)
#   original = open_image('THEIMAGE')
#
#   # Example Pixel Color
#   print('Color: ' + str(get_pixel(original, 0, 0)))
#
#   # Convert to Primary and save
#   new = convert_primary(original)
#   save_image(new, 'Prinny_primary.png')
