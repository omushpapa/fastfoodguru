from django.conf.urls import url, include
from . import views

app_name = 'accounts'
urlpatterns = [
	url(r'^$', views.profile, name='profile'),
	url(r'^edit/$', views.editprofile, name='editprofile'),
]