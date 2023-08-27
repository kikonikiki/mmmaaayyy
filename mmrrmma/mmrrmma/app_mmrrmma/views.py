from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# def index(request):
#     return render(request, 'index.html')
#
# def top_sellers(request):
#     return render(request, 'top-sellers.html')

from django.shortcuts import render, redirect
from .models import Mmrrmma
from django.contrib.auth.decorators import login_required
from app_mmrrmma.models import Mmrrmma
from django.contrib.auth import get_user_model
from django.db import connection
from django.db.models import Count
from .forms import AdvertisimetForm
from django.urls import reverse

User = get_user_model
def index(request):
    title = request.GET.get('query')
    if title:
        mmrrmmas = Mmrrmma.objects.filter(title__icontains=title)
    else:
        mmrrmmas = Mmrrmma.objects.all()
    context = {'mmrrmmas': mmrrmmas,
               'title':title
               }
    return render(request, 'index.html', context)

def mmrrmma_detail(request,pk):
    mmrrmma = Mmrrmma.objects.get(id= pk)
    context ={
        'mmrrmma':mmrrmma,
    }

    return render(request, 'advertisement.html', context)

def top_sellers(request):
    users = User.objects.annotate(
        adv_count=Count('mmrrmma').order_by('-adv_count')
    )
    context = {
        'users':users
    }
    return render(request, 'top-sellers.html', context)

def adv_post(request,):
    if request.method == 'POST':
        form = AdvertisimetForm(request.POST, request.FILES)
        if form.is_valid():
            mmrrmmas = Mmrrmma(**form.cleaned_data)
            mmrrmmas.user = request.user
            mmrrmmas.save()
            url = reverse('main-page')
            return redirect(url)

    else:
        form = AdvertisimetForm
        context = {'form':form}
        return render(request,'advertisiment-post-html', context)