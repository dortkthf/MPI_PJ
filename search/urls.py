from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static
from .views import *

urlpatterns = [
	path('', views.sales_report, name ='sales_report'),
	path('e404', views.e404, name='e404'),
	path('fetch_team_data/', fetch_team_data, name='fetch_team_data'),
]
