from django.http import HttpResponse
from django.shortcuts import render

from .image_service import *


def index(request):
    return render(request, 'index.html')

def effect(request):
    if request.method == 'POST' and request.FILES['inputFile'] and request.POST['effect']:

        filename = request.FILES['inputFile'].name[:-4]
        image = pill(request.FILES['inputFile'], request.POST['effect'])
        response = HttpResponse(image, content_type='application/*')
        response['Content-Disposition'] = f'attachment; filename="{filename}.png"'

        return response

    else:
        return render(request, 'index.html')


