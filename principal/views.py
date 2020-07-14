from django.http import StreamingHttpResponse
from django.shortcuts import render
from .image_service import pill


def index(request):
    return render(request, 'index.html')


def effect(request):
    if request.method == 'POST':

        file = request.FILES['inputFile']
        effect = request.POST['effect']
        filename = file.name[:-4]

        image = pill(file, effect)

        response = StreamingHttpResponse(image)
        response['Content-Length'] = image.size
        response['Content-Type'] = 'image/png'
        response['Status'] = 200
        response['Content-Disposition'] = f'attachment; filename="{filename}.png"'

        return response

    else:
        return render(request, 'index.html')


