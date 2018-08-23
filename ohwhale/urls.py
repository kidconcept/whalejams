from django.urls import path
from django.urls import include
from django.urls import re_path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('song/<uuid:pk>', views.RecordingDetailView.as_view(), name='song-detail'),
	path('song/upload/', views.upload, name='song-upload'),
]

# S3 Direct Test
urlpatterns += [
    re_path(r'^s3direct/', include('s3direct.urls')),
]

# djang-filters
urlpatterns += [
	re_path(r'^list$', views.song_list),
	path('songs/', views.song_list, name='songfilter'),
]