from email.message import EmailMessage
from django.shortcuts import render, redirect
from .forms import RegisterForm
from config.settings import EMAIL_HOST_PASSWORD, EMAIL_HOST_USER
from .models import *
from django.http import JsonResponse
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as dj_login
from django.contrib import messages
from django.core.paginator import Paginator
from .models import CampgroundImages
from django.core.mail import send_mail
from django.conf import settings








# Create your views here.
def home(request):
    campground_items = Campground.objects.all()
    campground_images = CampgroundImages.objects.all()
    amenities = Amenities.objects.all()

    cg_paginator = Paginator(campground_items, 5)

    page_num = request.GET.get('page')

    page = cg_paginator.get_page(page_num)


    context = {
        'campground_items': campground_items,
        'amenities' : amenities,
        'count': cg_paginator.count,
        'page': page,
        'campground_images': campground_images
    }

    return render(request, 'home.html', context)

def get_campground(request):
    try:
        campground_objs = Campground.objects.all()
        if request.GET.get('sort_by'):
            sort_by_value = request.GET.get('sort_by')
            if sort_by_value == 'asc':
                campground_objs = campground_objs.order_by('campground_price')
            elif sort_by_value == 'dsc':
                campground_objs = campground_objs.order_by('-campground_price')
        if request.Get.get('amount'):
            amount = request.GET.get('amount')
            campground_objs = campground_objs.filter(campground_price = amount)

        if request.Get.get('amenities'):
            amenities = request.Get.get('amenities')
            amenities = str(amenities).split(',')
            am = []
            for amenity in amenities:
                am.append(int(amenity))
            
            print(am)

            campground_objs = campground_objs.filter(amenities__in = am)



        payload = [] 
        for campground_obj in campground_objs:
            payload.append ({
                'campground_name' : campground_obj.campground_name,
                'campground_price' : campground_obj.campground_price,
                'description' : campground_obj.description,
                'banner_image': str(campground_obj.banner_image),
                'amenities': campground_obj.get_amenities(),
            })

        return JsonResponse (payload, safe=False)
    except Exception as e:
        print(e)

    return JsonResponse({'message': 'Something went wrong '})

 
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  
            # load the profile instance created by the signal
            user.save()
            raw_password = form.cleaned_data.get('password1')

            # login user after signing up
            user = authenticate(username=user.username, password=raw_password)
            dj_login(request, user)
        if request.method == 'POST':
            subject = request.POST.get('Test Email')
            message = request.POST.get('Test message')
            email = request.POST.get('email')
            send_mail(subject, message, settings.EMAIL_HOST_USER,
                  [email], fail_silently=False)
            return render(request, 'email.html', {'email': email}) 

            # redirect user to home page
        return redirect('profile')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})



def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            dj_login(request, user)
            return redirect('home')
        else:
            messages.success(request, ('Error, try again'))
            return redirect('login')
    else:
        return render(request, 'registration/login.html')



def profile(request):
    context = {'user': request.user}
    
    return render(request, 'profile.html', context)

def reviews(request):
    obj = Review.objects.filter(product=0).order_by("?").first()
    data = Campground.objects.all()
    context = {
        'object': obj,
        'data': data
    }

    return render(request, 'review.html', context, data)

def search(request):
    campground_objs  = Campground.objects.all()
    if request.Get.get('sort_by'):
        sort_by_value = request.Get.get('sort_by')
        if sort_by_value == 'asc':
            campground_objs = campground_objs.order_by('campground_price')
        elif sort_by_value == 'dsc':
            campground_objs = campground_objs.order_by('-campground_price')
        if request.Get.get('amount'):
            amount = request.Get.get('amount')
            campground_objs = campground_objs.filter(campground_price = amount)
        payload = [] 
        for campground_obj in campground_objs:
            payload.append ({
                'campground_name' : campground_obj.campground_name,
                'campground_price' : campground_obj.campground_price,
                'description' : campground_obj.description,
                'banner_image': campground_obj.banner_image,
                'amenities': campground_obj.get_amenites(),
            })
    return render (request, 'home', )


def ncpage(request):
    return render(request, 'ncpage.html')

def ncpage1(request):
    return render(request, 'ncpage1.html')

def images(request):
    images = CampgroundImages.objects.all()
    context = {
        'images': images
    }
    return render(request, 'home.html', context)


def send_email(request):
    if request.method == 'POST':
        subject = request.POST.get('Test Email')
        message = request.POST.get('Test message')
        email = request.POST.get('email')
        send_mail(subject, message, settings.EMAIL_HOST_USER,
                  [email], fail_silently=False)
        return render(request, 'email.html', {'email': email})

    return render(request, 'confirmation.html', {})

def confirmation(request):
    return render (request, 'confirmation.html')
    
