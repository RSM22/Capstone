from django.shortcuts import render
from .models import *
from django.http import JsonResponse

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

def register (request):
    return render (request, 'register.html')


def login (request):
    return render (request, 'login.html')

    