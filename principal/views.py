
from django.core.files.base import ContentFile
from django.shortcuts import render
from django.core.files.uploadedfile import InMemoryUploadedFile
from .image_service import *
from io import BytesIO
from django.http import HttpResponse

from django.core.files.uploadedfile import InMemoryUploadedFile
from django.shortcuts import render

from .image_service import *


def index(request):
    return render(request, 'index.html')

def effect(request):
    if request.method == 'POST' and request.FILES['inputFile'] and request.POST['effect']:

        filename = request.FILES['inputFile'].name[:-4]

        print(filename)
        image = pill(request.FILES['inputFile'], request.POST['effect'])
        response = HttpResponse(image, content_type='application/*')
        response['Content-Disposition'] = f'attachment; filename="{filename}.png"'

        return response



