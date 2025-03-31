from PIL import Image

image = Image.open('img.png')

rgbImage = image.convert('RGB')
width, height = rgbImage.size

starColor = (255, 255, 255)
meteorColor = (255, 0, 0)
waterColor = (0, 0, 255)

pixels = list(rgbImage.getdata())

stars = []
meteors = []
waterLevel = 0
fallOnWater = 0
waterColumns = set()

for x in range(width):
    for y in range(height):
        pixel = rgbImage.getpixel((x, y))
        if(pixel == waterColor):
            waterLevel = y
            break
        elif pixel == meteorColor:
            meteors.append((x,y))
        elif pixel == starColor:
            stars.append((x,y))

for x in range(width):
    pixel = rgbImage.getpixel((x, waterLevel))
    if(pixel == waterColor):
        waterColumns.add(x)

for meteorX in meteors:
    if meteorX[0] in waterColumns:
        fallOnWater += 1

print(f"Estrelas: {len(stars)}")
print(f"Meteoros: {len(meteors)}")
print(f"Meteoros caindo na água: {fallOnWater}")