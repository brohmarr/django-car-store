from django.http import HttpResponse


def cars_view(request):
    return HttpResponse('<h1>Web Cars</h1>')
