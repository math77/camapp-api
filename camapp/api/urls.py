from django.conf.urls import url
from django.urls import include, path
from . import views

urlpatterns = [
		url(r'^users/$', views.UserList.as_view(), name='user-list'),
		url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),

		url(r'^events/$', views.EventList.as_view(), name='event-list'),
		url(r'^events/(?P<pk>[0-9]+)/$', views.EventDetail.as_view(), name='event-detail'),

		url(r'^types_events/$', views.TypeEventList.as_view(), name='type-event-list'),
		
		url(r'^posts/$', views.PostList.as_view(), name='post-list'),
		url(r'^posts/(?P<pk>[0-9]+)/$', views.PostDetail.as_view(), name='post-detail'),

		url(r'^followers/$', views.FollowerList.as_view(), name='follower-list'),
		url(r'^followers/(?P<pk>[0-9]+)/$', views.FollowerDetail.as_view(), name='follower-detail'),
		
		url(r'^comments/$', views.PostCommentList.as_view(), name='comments-list'),
		url(r'^comments/(?P<pk>[0-9]+)/$', views.PostCommentDetail.as_view(), name='comment-detail'),

		url(r'^configs/(?P<pk>[0-9]+)/$', views.ConfigEventDetail.as_view(), name='config-datails'),
]