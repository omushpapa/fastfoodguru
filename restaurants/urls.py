from django.conf.urls import url
from . import views

app_name = 'restaurants'
urlpatterns = [
	url(r'^all/$', views.ListRestaurants.as_view(), name='list_restaurants'),
	url(r'^new/$', views.AddRestaurant.as_view(), name='add_restaurant'),
	url(r'^(?P<rest_id>[\d]+)/update/$', views.UpdateRestaurant.as_view(), name='update_restaurant'),
]