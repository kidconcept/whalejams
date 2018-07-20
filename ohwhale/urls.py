from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('s3test', views.DocumentCreateView.as_view(), name="s3test")
]