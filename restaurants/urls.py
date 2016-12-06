from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'restaurants'
urlpatterns = [
	url(r'^all/$', login_required(views.ListRestaurants.as_view()), name='list_restaurants'),
	url(r'^new/$', login_required(views.AddRestaurant.as_view()), name='add_restaurant'),
	url(r'^(?P<rest_id>[\d]+)/update/$', login_required(views.UpdateRestaurant.as_view()), name='update_restaurant'),
]