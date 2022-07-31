from distutils.command.upload import upload
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
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
    
    def get_amenites(self):
        payload = []

        for amenity in self.amenity_name.all():
            payload.append({'id': amenity.id, 'amenity': amenity.amenity})
        return payload


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

    def __str__(self):
        return self.campground



class CampgroundBooking(BaseModel):
    campground = models.ForeignKey(Campground, related_name="campground_booking", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="user_booking", on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    booking_type = models.CharField(max_length=100, choices=(('Pre Paid', 'Pre Paid'), ('Post Paid', 'Post Paid')))

    


class SiteUsers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    profile_picture = models.ImageField(default='', null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Campground, models.CASCADE)
    comment = models.TextField(max_length=250)
    rate = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0),
        ]
    )
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.pk)


