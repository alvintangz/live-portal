from django.contrib.auth.hashers import is_password_usable
from django import forms
from .models import User, Delegate

class DelegateUserForm(forms.ModelForm):
	class Meta:
		model = User
		# remove password option later
		exclude = ['is_partner', 'is_delegate', 'is_superuser', 'is_staff', 'groups', 'user_permissions', 'last_login', 'username']

	def __init__(self, *args, **kwargs):
		super(DelegateUserForm, self).__init__(*args, **kwargs)
		self.fields['email'].required = True

	def save(self, commit=True):
		user = super(DelegateUserForm, self).save(commit=False)
		user.set_delegate()
		# Set the username as the email
		user.username = self.cleaned_data["email"]
		if commit:
			user.save()
		return user

class PartnerUserForm(forms.ModelForm):
	class Meta:
		model = User
		# remove password option later
		exclude = ['is_partner', 'is_delegate', 'is_superuser', 'is_staff', 'groups', 'user_permissions', 'last_login']

	def save(self, commit=True):
		user = super(PartnerUserForm, self).save(commit=False)
		user.set_partner()
		if commit:
			user.save()
		return user

# Form with all basic user information
class DelegateUserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email')

class DelegateProfileForm(forms.ModelForm):
	class Meta:
		model = Delegate
		fields = ('profile_picture', 'year_of_study', 'school', 'program', 'linkedin', 'resume', 'phone_number', 'seeking_status')