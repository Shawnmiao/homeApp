from django.shortcuts import render

def index(request):
    return render(request, 'homeApp/index.html', {})


# Create your views here.
