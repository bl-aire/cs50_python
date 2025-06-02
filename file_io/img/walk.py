import sys

from PIL import Image

images = []

# sys argument include the file name and the images. 1: means leave out the file name
# "python walk.py walk1.png walk2.png walk3.png walk4.png"
# LOOK FOR SUITABLE IMAGES

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

images[0].save(
    "walk.gif",
    save_all=True,
    append_images=[images[1]],
    duration=200,
    loop=0,
)