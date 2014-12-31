from django import forms
from signup.models import UserProfile
from django.contrib.auth.models import User


class UserProfileForm(forms.ModelForm):

	class Meta:
		model = UserProfile
		fields = ('user_group','tagline')

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('email','password')
