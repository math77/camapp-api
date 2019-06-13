from django.contrib import admin
from .models import Event, Post, PostComment, Follower, PostEvent, UserVideo, TypeEvent

# Register your models here.
admin.site.register(Event)
admin.site.register(Post)
admin.site.register(PostComment)
admin.site.register(Follower)
admin.site.register(PostEvent)
admin.site.register(UserVideo)
admin.site.register(TypeEvent)