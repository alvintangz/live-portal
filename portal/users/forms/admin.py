from django import forms
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from users.models import User, Delegate

# TO BE DELETED

class AdminDelegateUserForm(UserChangeForm):
	class Meta:
		model = User
		exclude = ['is_partner', 'is_delegate', 'is_superuser', 'is_staff',
		'groups', 'user_permissions', 'last_login']

	def save(self, commit=True):
		user = super(AdminDelegateUserForm, self).save(commit=False)
		user.set_delegate()
		if commit:
			user.save()
		return user

class AdminPartnerUserForm(forms.ModelForm):
	class Meta:
		model = User
		# remove password option later
		exclude = ['is_partner', 'is_delegate', 'is_superuser', 'is_staff',
		'groups', 'user_permissions', 'last_login']

	def save(self, commit=True):
		user = super(AdminPartnerUserForm, self).save(commit=False)
		user.set_partner()
		if commit:
			user.save()
		return user