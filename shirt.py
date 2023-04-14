import sys
import PIL
from PIL import Image, ImageOps
import os


if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")


image_path = sys.argv[1].lower()
photo_path = sys.argv[2].lower()
shirt_path = "shirt.png".lower()

if not image_path.endswith(".png") and not image_path.endswith(".jpg") and not image_path.endswith(".jpeg"):
    sys.exit("Invalid input")
if not photo_path.endswith(".png") and not photo_path.endswith(".jpg") and not photo_path.endswith(".jpeg"):
    sys.exit("Invalid input")


end1 = os.path.splitext(image_path)
end2 = os.path.splitext(photo_path)

if end1[1] != end2[1]:
    sys.exit("Input and output have different extensions")

try:
    image = PIL.Image.open(image_path)
    shirt = PIL.Image.open(shirt_path)
except FileNotFoundError:
    sys.exit("Input does not exist")

size = shirt.size
resized_image = PIL.ImageOps.fit(image, size)

resized_image.paste(shirt, (0, 0), shirt)
resized_image.save(photo_path, format="JPEG")
