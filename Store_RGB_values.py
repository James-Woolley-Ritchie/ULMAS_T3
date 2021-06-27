# Imageio for image analysis.
import imageio

# Open a text file to keep the RGB data in.
text_write = open("Stuff_in_here.txt", "w")

# The first bunch of images.
for image_number in range(72 - 28):
    print(image_number)
    image = imageio.imread("photo_{}.jpg".format("0" + str(28 + image_number)))
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            # The RGB values of the pixel will go in here.
            pixel = []
            pixel.append(image[y, x, 0]) # Red.
            pixel.append(image[y, x, 1]) # Green.
            pixel.append(image[y, x, 2]) # Blue
            text_write.write("{}, {}, {}\n".format(str(pixel[0]), str(pixel[1]), str(pixel[2])))

# The second bunch of images.
for image_number in range(163 - 119):
    print(image_number)
    image = imageio.imread("photo_{}.jpg".format(119 + image_number))
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            # The RGB values of the pixel will go in here.
            pixel = []
            pixel.append(image[y, x, 0]) # Red.
            pixel.append(image[y, x, 1]) # Green.
            pixel.append(image[y, x, 2]) # Blue
            text_write.write("{}, {}, {}\n".format(str(pixel[0]), str(pixel[1]), str(pixel[2])))

# Close the text file.
text_write.close()
