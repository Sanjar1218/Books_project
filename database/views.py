from django.shortcuts import render
from .models import Books

def home(request):
    data = Books.objects.all()
    print(data)
    return render(request, 'pages/home.html', context={'data': data})