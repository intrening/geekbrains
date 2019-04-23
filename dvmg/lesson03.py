from PIL import Image

def shift_color(image, shift):
    if shift > 0:
        coords_crop = (shift*2, 0, image.width, image.height)
    else:
        shift = - shift
        coords_crop = (0, 0, image.width-shift*2, image.height)
    image_crop = image.crop(coords_crop)

    coords2 = (shift, 0, image.width-shift, image.height)
    image2 = image.crop(coords2)
    image_new = Image.blend(image2,image_crop,0.5)
    return image_new

image = Image.open("monro.jpg")
image = image.convert("RGB")

red,green,blue = image.split()

shift = 20
red = shift_color (red, shift)
blue = shift_color (blue, -shift)
green = green.crop((shift,0,green.width-shift,green.height))

image_new = Image.merge('RGB',(red,green,blue))
image_new.thumbnail((80,80))
image_new.save('monro2.jpg')
