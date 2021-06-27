# Open the text files.
text_read = open("Images.txt", "r")
text_write = open("No_black.txt", "w")
for pixel in text_read:
    current_pixel = pixel.strip("\n").split(",")
    # Black max -> 76, 78, 77
    if not (int(current_pixel[0]) <= 42 and int(current_pixel[1]) <= 82 and int(current_pixel[2]) <= 108):
        text_write.write(pixel)

# Close the text files.
text_read.close()
text_write.close()
