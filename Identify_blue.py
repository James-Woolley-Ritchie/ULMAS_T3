# Is a colour classed as blue.
def Is_blue(red, green, blue):
    # These parameters are to be changed.
    if (red <= 100 and green <= 150 and blue > green + 10 and green > red + 10):
        return True
    else:
        return False

# Open the file.
text_read = open("No_black.txt", "r")

# Check all of the pxels to see what percentage of them are blue.
number_of_pixels = 0
number_of_blue_pixels = 0
for pixel in text_read:
    number_of_pixels += 1
    red = int(pixel.strip("\n").split(",")[0])
    green = int(pixel.strip("\n").split(",")[1])
    blue = int(pixel.strip("\n").split(",")[2])
    if (Is_blue(red, green, blue)):
        number_of_blue_pixels += 1

# Give the results.
print("\nNumber of pixels checked: {}".format(number_of_pixels))
print("Number of pixels registered as blue: {}".format(number_of_blue_pixels))
print("Percentage of pixels registered as blue: {}\n".format((number_of_blue_pixels / number_of_pixels) * 100))
