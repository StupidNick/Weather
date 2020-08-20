from django.urls import path
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


app_name = 'weatherManager'
urlpatterns = [
	# path('', views.index, name = 'index'),
	# path('<int:city_id>/', views.detail, name = 'detail'),
	# path('<int:city_id>/add_temperature/', views.add_temperature, name = 'add_temperature'),
	# path('add_city', views.add_city, name = 'add_city'),
	# path('create_city', views.create_city, name = 'create_city'),
	# path('<int:city_id>/filter_temperature', views.filter_temperature, name = 'filter_temperature'),
	# path('<int:temp_id>/edit_temperature/', views.edit_temperature, name = 'edit_temperature'),
	# path('<int:temp_id>/edit/', views.edit, name = 'edit'),
	path('city/', views.CityList.as_view(), name = 'city'),
	path('city/<int:city_id>/', views.CityDetail.as_view(), name = 'CityDetail'),
	path('temperature/<int:cityes_id>/', views.TempList.as_view(), name = 'tempList'),
	path('temperature/<int:cityes_id>/<int:temp_id>/', views.TempDetail.as_view(), name = 'tempDetail'),
	path('temperature/<int:cityes_id>/<filter1>/', views.DateFilter, name = 'DateFilter'),
]

urlpatterns = format_suffix_patterns(urlpatterns)