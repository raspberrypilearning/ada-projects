import PIL.Image
import math
# Create a new image
image = PIL.Image.open('shrek.jpeg')
print(image.info)
new_data = []
sepia_data = []
posterized_data = []
for pixel in image.getdata():
    print(pixel)
    new_data.append(sum(pixel) / 3)
    d = 50
    posterized_data.append((pixel[0] // d * d, pixel[1] // d * d, pixel[2] // d * d))
    (originalR, originalG, originalB) = pixel
    newR = math.floor(originalR * .393 + originalG * .769 + originalB * .189)
    newG = math.floor(originalR * .349 + originalG * .686 + originalB * .168)
    newB = math.floor(originalR * .272 + originalG * .534 + originalB * .131)
    sepia_data.append((newR, newG, newB))

new_image = PIL.Image.new('L', image.size)
new_image.putdata(new_data)

sepia_image = PIL.Image.new('RGB', image.size)
sepia_image.putdata(sepia_data)
sepia_image.save('sepia.jpg')

posterized_image = PIL.Image.new('RGB', image.size)
posterized_image.putdata(posterized_data)
posterized_image.save('posterized.jpg')


# Save the image to a file named random.jpg.
new_image.save('random.jpg')
# Click on the random.jpg tab at the top to see the resulting image.
# Keep clicking run when you're on the tab to see the image change.
# Try changing the size of the image and the number of random
# colors and see how the image changes.