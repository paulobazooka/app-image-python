from PIL import Image, ImageOps
import PIL.ImageOps

"""
Retorna a imagem em sepia
"""
def sepia(img:Image)->Image:
    width, height = img.size

    pixels = img.load() # create the pixel map

    for py in range(height):
        for px in range(width):

            if img.mode == 'RGBA':
                r, g, b ,a = img.getpixel((px, py))

                tr = int(0.393 * r + 0.769 * g + 0.189 * b)
                tg = int(0.349 * r + 0.686 * g + 0.168 * b)
                tb = int(0.272 * r + 0.534 * g + 0.131 * b)

                if tr > 255:
                    tr = 255

                if tg > 255:
                    tg = 255

                if tb > 255:
                    tb = 255

                pixels[px, py] = (tr,tg,tb, 255)

            else:
                r, g, b = img.getpixel((px, py))

                tr = int(0.393 * r + 0.769 * g + 0.189 * b)
                tg = int(0.349 * r + 0.686 * g + 0.168 * b)
                tb = int(0.272 * r + 0.534 * g + 0.131 * b)

                if tr > 255:
                    tr = 255

                if tg > 255:
                    tg = 255

                if tb > 255:
                    tb = 255

                pixels[px, py] = (tr, tg, tb)

    return img

"""
Retorna a imagem em preto e branco
"""
def bw(im: Image)->Image:
    return PIL.ImageOps.grayscale(im)

def negative(im: Image)->Image:
    image = None
    if im.mode != 'RGB':
        image = im.convert('RGB')
    else:
        image = im

    return ImageOps.invert(image)
