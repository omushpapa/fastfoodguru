from django.conf.urls import url, include
from . import views

app_name = 'accounts'
urlpatterns = [
	url(r'^$', views.profile, name='profile'),
	url(r'^edit/$', views.editprofile, name='editprofile'),
	url(r'^register/$', views.register, name='register'),
	url(r'^logout/$', views.logout_user, name='logout'),
	url(r'^login/$', views.login_user, name='login'),
]