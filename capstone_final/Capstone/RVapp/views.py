from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as dj_login




# Create your views here.
def home(request):
    return render(request, 'home.html')

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


        payload = [] 
        for campground_obj in campground_objs:
            payload.append ({
                'campground_name' : campground_obj.campground_name,
                'campground_price' : campground_obj.campground_price,
                'description' : campground_obj.description,
                'banner_image': str(campground_obj.banner_image),
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

            # redirect user to home page
            return redirect('profile')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def profile(request):
    context = {'user': request.user}
    
    return render(request, 'profile.html', context)

def login (request):
    return render (request, 'login.html')

    