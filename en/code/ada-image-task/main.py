import PIL.Image
import random
image = PIL.Image.new('RGB', (100, 100))

for x in range(100):
  for y in range(100):
    pos = (x,y)
    red = random.randint(0,255)
    green =  random.randint(0,255)
    blue =  125
    color = (red,green,blue)
    image.putpixel(pos,color)
print("image created")
image.save("test.jpg")
