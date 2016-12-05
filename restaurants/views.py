from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Restaurant
from django.core.urlresolvers import reverse_lazy

class ListRestaurants(ListView):
	model = Restaurant
	template_name = 'restaurants/restaurant_list.html'
	context_object_name = 'restaurant_list'

class AddRestaurant(CreateView):
	model = Restaurant
	fields = ('name', 'description','country', 'state', 'city', 'street',)
	template_name = 'restaurants/add_restaurant.html'
	success_url = reverse_lazy('restaurants:list_restaurants')