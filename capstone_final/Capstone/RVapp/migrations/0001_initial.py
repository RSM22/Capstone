# Generated by Django 4.0.5 on 2022-07-23 14:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Amenities',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('amenity_name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Campground',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('campground_name', models.CharField(max_length=200)),
                ('campground_price', models.IntegerField()),
                ('description', models.TextField()),
                ('space_count', models.IntegerField(default=10)),
                ('banner_image', models.ImageField(upload_to='campgrounds')),
                ('amenities', models.ManyToManyField(to='RVapp.amenities')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CampgroundImages',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('images', models.ImageField(upload_to='campgrounds')),
                ('campground', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='campground_images', to='RVapp.campground')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CampgroundBooking',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('booking_type', models.CharField(choices=[('Pre Paid', 'Pre Paid'), ('Post Paid', 'Post Paid')], max_length=100)),
                ('campground', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='campground_booking', to='RVapp.campground')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_booking', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
