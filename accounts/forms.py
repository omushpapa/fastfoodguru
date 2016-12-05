from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UserRegistrationForm(UserCreationForm):

	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'username','email')


	def save(self, commit=True):
		user = super(UserRegistrationForm, self).save(commit=False)
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.username = self.cleaned_data['username']
		user.email = self.cleaned_data['email']

		if commit:
			user.save()

		return user

class LoginForm(AuthenticationForm):
	username = forms.CharField(max_length=30)
	password = forms.CharField(max_length=30, widget=forms.PasswordInput())