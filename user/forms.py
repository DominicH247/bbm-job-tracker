from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

	class Meta(UserCreationForm):
		model = CustomUser
		fields = UserCreationForm.Meta.fields + ('first_name','last_name', 'Position',)
		

class CustomUserChangeForm(UserChangeForm):
	"""user update form"""
	#  UserChangeForm has password field as defult (declared)
	#  must override it
	password = None

	class Meta:
		model = CustomUser
		fields = (
			'username', 
			'email', 
			'first_name', 
			'last_name', 
			'Position',
		)

		