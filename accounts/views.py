from django.shortcuts import render
from django.http import HttpResponse

def profile(request):
	#return HttpResponse("Profile page.")
	return render(request, 'accounts/profile.html')

def editprofile(request):
	return render(request, 'accounts/editprofile.html')
