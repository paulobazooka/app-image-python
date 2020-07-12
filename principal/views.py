from django.core.files.storage import FileSystemStorage
from io import BytesIO
from django.core.files.base import ContentFile
from django.shortcuts import render
from PIL import Image, ImageFilter, ImageOps
from django.core.files.uploadedfile import InMemoryUploadedFile

def index(request):
    return render(request, 'index.html')

def effect(request):
    if request.method == 'POST' and request.FILES['inputFile']:
        image = pill(request.FILES['inputFile'])
        image_file = InMemoryUploadedFile(image, None, 'foto_alterada.jpg', 'image/png', image.tell, None)

        print(f'Formato da imagem {type(image)}')
        print(f'Formato da imagem processada {type(image_file)}')

        """myfile = request.FILES['inputFile']
        print(type(myfile))
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        path = settings.MEDIA_ROOT + '/' + filename
        image = Image.open(path)

        im_sharp = image.filter(ImageFilter.SHARPEN)
        # Saving the filtered image to a new file
        im_sharp.save(filename, 'JPEG')

        uploaded_file_url = fs.url(filename)"""
        return render(request, 'index.html', {
            'uploaded_file_url': ''
        })
    return render(request, 'index.html')


def pill(image_io):
    im = Image.open(image_io)
    ltrb_border = (0, 0, 0, 10)
    im_with_border = ImageOps.expand(im, border=ltrb_border, fill='white')
    im.rotate(90)

    buffer = BytesIO()
    im_with_border.save(fp=buffer, format='PNG')
    buff_val = buffer.getvalue()
    return ContentFile(buff_val)
