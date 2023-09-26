from django.shortcuts import render


def home(request):
    return render(request, 'portfolio/index.html')
# Create your views here.
