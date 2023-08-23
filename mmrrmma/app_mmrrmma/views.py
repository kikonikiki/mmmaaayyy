from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# def index(request):
#     return render(request, 'index.html')
#
# def top_sellers(request):
#     return render(request, 'top-sellers.html')

from django.shortcuts import render
from .models import Mmrrmma


def index(request):
    advertisements = Mmrrmma.objects.all() # вытаскиваем все данные из бд
    context = {'advertisements': advertisements}
    return render(request, 'index.html', context)


def top_sellers(request):
    return render(request, 'top-sellers.html')