from django.urls import path
from django.urls import include
from django.urls import re_path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('song/<uuid:pk>', views.RecordingDetailView.as_view(), name='song-detail'),
	#path('songs/', views.RecordingListView.as_view(), name='songs'),
	path('song/upload/', views.RecordingCreate.as_view(), name='song-upload'),
	#path('recording/<int:pk>/update/', views.RecordingUpdate.as_view(), name='recording_update'),
    #path('recording/<int:pk>/delete/', views.RecordingDelete.as_view(), name='recording_delete'),
]

urlpatterns += [
	re_path(r'^progressbarupload/', include('progressbarupload.urls'))
]