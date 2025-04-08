import imageio.v3 as iio

fileNames = [
    "image(1).jpg",
    "image(2).jpg",
    "image(3).jpg",
    "image(4).jpg",
]
images = []

# Create a GIF from the images
for fileNames in fileNames:
    images.append(iio.imread(fileNames))

# Save the images as a GIF
iio.imwrite("output.gif", images, duration=1000, loop = 0) # 1 second per frame