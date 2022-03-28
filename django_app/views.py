from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    data = {
        'request_type': request.method,
        'name': 'Tom',
    }
    if request.method == 'GET':
        return render(request, 'django_app/index.html', data)
    else:
        return HttpResponse('<h1>Not a GET request</h1>')
