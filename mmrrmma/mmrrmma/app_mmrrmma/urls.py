from django.urls import path
from .views import index, top_sellers, adv_post, mmrrmma_detail

urlpatterns = [
    path('', index, name='main-page'),
    path('top-sellers/', top_sellers, name='top-sellers'),
    path('adv-post/',adv_post, name='adv-post'),
    path('mmrrmma/<int:pk>',mmrrmma_detail, name='mmrr-detail'),
]