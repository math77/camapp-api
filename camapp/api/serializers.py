from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from .models import User, Profile, Event, TypeEvent, Post, UserVideo, Follower, PostEvent, PostComment, ConfigEvent

"""
Verificar os serializers que possuem mídia. Forma correta de serializar
"""

class ProfileUserSerializer(WritableNestedModelSerializer):
	class Meta:
		model = Profile
		exclude = ('profile_pic', 'user',)


class UserSerializer(WritableNestedModelSerializer):
	profile = ProfileUserSerializer()
	class Meta:
		model = User
		fields = ('username', 'email', 'password', 'first_name', 'last_name', 'profile')


class EventSerializer(serializers.ModelSerializer):
	class Meta:
		model = Event
		fields = '__all__'


class ConfigEventSerializer(serializers.ModelSerializer):
	class Meta:
		model = ConfigEvent
		fields = '__all__'


class TypeEventSerializer(serializers.ModelSerializer):
	class Meta:
		model = TypeEvent
		fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = '__all__'


class UserVideoSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserVideo
		fields = '__all__'


class FollowerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Follower
		fields = '__all__'


class PostEventSerializer(serializers.ModelSerializer):
	class Meta:
		model = PostEvent
		fields = '__all__'


class PostCommentSerializer(serializers.ModelSerializer):
	class Meta:
		model = PostComment
		fields = '__all__'