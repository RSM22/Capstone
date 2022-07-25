from django.contrib import admin
from .models import *
# Register your models here.
class CampgroundAdmin(admin.ModelAdmin):
    list_display = [
        'campground_name', 'campground_price', 'description'
    ]

admin.site.register(Amenities)
admin.site.register(Campground, CampgroundAdmin)
admin.site.register(CampgroundImages)
admin.site.register(SiteUsers)