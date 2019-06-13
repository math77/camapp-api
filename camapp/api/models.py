from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.TextField(max_length=500, blank=True, null=True)
	phone = models.CharField(max_length=13, null=False, blank=False)
	profile_pic = models.ImageField(upload_to='profile_pic_folder/', null=True)
	date_birth = models.DateField(null=True)
	street_address = models.CharField(max_length=100, null=False)
	number_address = models.CharField(max_length=7, null=False)
	city_address = models.CharField(max_length=100, null=False)
	zipcode_address = models.CharField(max_length=9, null=False)
	district_address = models.CharField(max_length=100, null=False)
	complement_address = models.CharField(max_length=150, null=True)
	talent_program = models.BooleanField(default=False)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class TypeEvent(models.Model):
	name = models.CharField(max_length=50, null=False)
	description = models.CharField(max_length=150, null=False)


class Event(models.Model):
	event_name = models.CharField(max_length=100, null=False)
	description = models.TextField()
	id_type_event = models.ForeignKey(TypeEvent, on_delete=models.PROTECT, null=False)
	id_user_owner = models.ForeignKey(User, on_delete=models.PROTECT, null=False)
	start_time = models.DateTimeField(null=False)
	end_time = models.DateTimeField()
	is_private = models.BooleanField(default=False)
	location_latitude = models.FloatField()
	location_longitude = models.FloatField()
	qrcode_advertising = models.CharField(max_length=100, blank=False, null=True, unique=True)


class ConfigEvent(models.Model):
	who_can_view = models.PositiveIntegerField(null=False)
	who_can_post = models.PositiveIntegerField(null=False)
	who_can_interact = models.PositiveIntegerField(null=False)
	who_can_invite = models.PositiveIntegerField(null=False)
	id_event = models.OneToOneField(Event, on_delete=models.CASCADE, null=False)


class Post(models.Model):
	video_post = models.FileField(upload_to='videos/', null=False)
	upload_date = models.DateTimeField(null=False, auto_now_add=True)
	is_private = models.BooleanField(default=False)
	id_user = models.ForeignKey(User, on_delete=models.PROTECT, null=False)


class UserVideo(models.Model):
	id_post = models.ForeignKey(Post, on_delete=models.PROTECT, null=False)
	id_user = models.ForeignKey(User, on_delete=models.PROTECT, null=False)
	date_viewed = models.DateTimeField(null=False)
	duration_viewed = models.TimeField(null=False)


class Follower(models.Model):
	id_follower = models.ForeignKey(User, on_delete=models.PROTECT, null=False, related_name="who_follows")
	id_following = models.ForeignKey(User, on_delete=models.PROTECT, null=False, related_name="who_is_followed")
	date_start_follow = models.DateTimeField(null=False, auto_now_add=True)


class PostEvent(models.Model):
	id_event = models.ForeignKey(Event, on_delete=models.PROTECT, null=False)
	id_post = models.ForeignKey(Post, on_delete=models.PROTECT, null=False)
	post_date = models.DateTimeField(null=False, auto_now_add=True)


class PostComment(models.Model):
	date = models.DateTimeField(null=False, auto_now_add=True)
	body_comment = models.TextField(null=False, blank=False)
	id_user = models.ForeignKey(User, on_delete=models.PROTECT, null=False)
	id_post = models.ForeignKey(Post, on_delete=models.PROTECT, null=False)


objects = models.Manager()