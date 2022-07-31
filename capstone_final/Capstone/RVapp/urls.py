from .views import *
from django.urls import path
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('campground/', views.get_campground, name='campground'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('ncpage/', views.ncpage, name='ncpage'),
    path('ncpage1/', views.ncpage1, name='ncpage1'),
    path('reviews', views.reviews, name="reviews"),
      
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

