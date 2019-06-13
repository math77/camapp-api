from django.shortcuts import render
from rest_framework import generics
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from . import models
from . import serializers
# Create your views here.

class UserList(generics.ListCreateAPIView):
	queryset = models.User.objects.all().prefetch_related('profile').order_by('id')
	serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = models.User.objects.all().prefetch_related('profile')
	serializer_class = serializers.UserSerializer


class EventList(generics.ListCreateAPIView):
	queryset = models.Event.objects.all().order_by('id')
	serializer_class = serializers.EventSerializer


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = models.Event.objects.all().prefetch_related('profile')
	serializer_class = serializers.EventSerializer


class ConfigEventDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = models.ConfigEvent.objects.all()
	serializer_class = serializers.ConfigEventSerializer


class TypeEventList(generics.ListCreateAPIView):
	queryset = models.TypeEvent.objects.all().order_by('id')
	serializer_class = serializers.TypeEventSerializer


class PostList(APIView):
	parser_classes = (MultiPartParser, FormParser)

	def get(self, request, format=None):
		posts = models.Post.objects.all().order_by('id')
		serializer_class = serializers.PostSerializer(posts, many=True)
		return Response(serializer_class.data)

	def post(self, request, *args, **kwargs):
		serializer_class = serializers.PostSerializer(data=request.data)
		if serializer_class.is_valid():
			serializer_class.save()
			return Response(serializer_class.data, status=status.HTTP_201_CREATED)
		return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetail(APIView):

	def get_object(self, pk):
		try:
			return models.Post.objects.get(pk=pk)
		except Post.DoesNotExist:
			raise Http404


	def get(self, request, pk, format=None):
		post = self.get_object(pk)
		serializer_class = serializers.PostSerializer(post)
		return Response(serializer_class.data)


	def put(self, request, pk, format=None):
		post = self.get_object(pk)
		serializer_class = serializers.PostSerializer(post, data=request.data)
		if serializer_class.is_valid():
			serializer_class.save()
			return Response(serializer_class.data)
		return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)


	def delete(self, request, pk, format=None):
		post = self.get_object(pk)
		post.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


class UserVideoList(generics.ListCreateAPIView):
	queryset = models.UserVideo.objects.all().order_by('id')
	serializer_class = serializers.UserVideoSerializer


class UserVideoDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = models.UserVideo.objects.all()
	serializer_class = serializers.UserVideoSerializer


class FollowerList(generics.ListCreateAPIView):
	queryset = models.Follower.objects.all().order_by('id')
	serializer_class = serializers.FollowerSerializer


class FollowerDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = models.Follower.objects.all()
	serializer_class = serializers.FollowerSerializer


class PostEventList(generics.ListCreateAPIView):
	queryset = models.PostEvent.objects.all().order_by('id')
	serializer_class = serializers.PostEventSerializer


class PostCommentList(generics.ListCreateAPIView):
	serializer_class = serializers.PostCommentSerializer

	def get_queryset(self):
		id_post = self.request.query_params.get('idPost')
		return models.PostComment.objects.filter(id_post=id_post).order_by('date')


class PostCommentDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = models.PostComment.objects.all()
	serializer_class = serializers.PostCommentSerializer