from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .forms import *

def profile(request):
	#return HttpResponse("Profile page.")
	return render(request, 'accounts/profile.html')

def editprofile(request):
	return render(request, 'accounts/editprofile.html')

def register(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect(reverse('accounts:profile'))

	if request.method == 'POST':
		form = UserRegistrationForm(request.POST)

		if form.is_valid():
			user = form.save()

			user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password1'))
			login(request, user)

			success_message = "Welcome %s! You have been logged in. " % form.cleaned_data.get('username').title()
			messages.success(request, success_message)

			return HttpResponseRedirect(reverse('home_page'))
		
		messages.error(request, 'Registration failed! Check listed errors.')

	else:
		form = UserRegistrationForm()


	return render(request, 'accounts/register.html',{'form': form, })

def logout_user(request):
	logout(request)
	messages.success(request, 'You have been logged out!')

	return HttpResponseRedirect(reverse('home_page'))

def login_user(request):
	next_page = request.GET['next']
	if request.user.is_authenticated():
		return HttpResponseRedirect(reverse('home_page'))

	if request.method == 'POST':
		form = LoginForm(data=request.POST)

		if form.is_valid():
			user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))

			if user is not None:
				if user.is_active:
					login(request, user)

					success_message = 'Welcome, %s.' % form.cleaned_data.get('username').title()
					messages.success(request, success_message)
					if next_page:
						return HttpResponseRedirect(next_page)
						
					return HttpResponseRedirect(reverse('home_page'))

		messages.error(request, 'Login failed! Username/password invalid.')

	else:
		form = LoginForm()

	return render(request, 'accounts/login.html', {'form': form, })