from django.db import models

# Create your models here.

from statistics import mode
from django.contrib.auth.models import User
from django.db import models
import uuid

# Create your models here.
class BaseModel(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Amenities(BaseModel):
    amenity_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.amenity_name

class Campground(BaseModel):
    campground_name = models.CharField(max_length=200)
    campground_price = models.IntegerField()
    description = models.TextField()
    amenities = models.ManyToManyField(Amenities)
    space_count = models.IntegerField(default=10)
    banner_image = models.ImageField(upload_to="campgrounds")

    def __str__(self) -> str:
        return self.campground_name

class CampgroundImages(BaseModel):
    campground = models.ForeignKey(Campground, related_name="campground_images", on_delete=models.CASCADE)
    images = models.ImageField(upload_to="campgrounds")



class CampgroundBooking(BaseModel):
    campground = models.ForeignKey(Campground, related_name="campground_booking", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="user_booking", on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    booking_type = models.CharField(max_length=100, choices=(('Pre Paid', 'Pre Paid'), ('Post Paid', 'Post Paid')))
