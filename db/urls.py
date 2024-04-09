from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static
from .views import *

urlpatterns = [
	path('', views.upload_file_view, name ='index'),    
]
