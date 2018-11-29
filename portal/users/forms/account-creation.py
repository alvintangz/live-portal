from django.contrib.auth.hashers import make_password
from django import forms
from users.models import Delegate
from users.helpers import generate_username
import re

def generate_username(first, last):
	users = User.objects.all()
	counter = 1
	good = False
	while(not good):
		username = (first + last)[:8] + counter
		good = True
		for user in users:
			if username == user.username:
				good = False
		counter += 1
	return username

class DelegateCreateForm(forms.ModelForm):
	"""A form with basic delegate information."""
	first_name = forms.CharField(max_length=30)
	last_name = forms.CharField(max_length=30)
	email = forms.EmailField()

	class Meta:
		model = Delegate
		fields = ['year_of_study', 'school', 'program', 
		'linkedin', 'resume', 'phone_number', 'seeking_status']

	def is_valid(self):
		valid = super(DelegateProfileUpdateForm, self).is_valid()

		# Return if not valid anyways
		if not valid:
			return valid

		# If linkedin profile is not blank
		if self.cleaned_data['linkedin'] != "":
			# Regex from: https://bit.ly/2zY11AG
			regex = "^https:\\/\\/[a-z]{2,3}\\.linkedin\\.com\\/.*$"
			if not re.match(regex, self.cleaned_data['linkedin']):
				return not valid

		# If phone number is not blank
		if self.cleaned_data['phone_number'] != "":
			try:
				num = int(self.cleaned_data['phone_number'])
				if not len(str(num)) == 10:
					return not valid
			except ValueError:
				return not valid

		# Just return valid
		return valid

	def save(self):
		instance = super(DelegateCreateForm, self).save()
		self.instance.user.first_name = self.cleaned_data["first_name"]
		self.instance.user.last_name = self.cleaned_data["last_name"]
		self.instance.user.email = self.cleaned_data["email"]
		self.instance.user.username = generate_username(self.cleaned_data["first_name"], self.cleaned_data["last_name"])
		rand_str = lambda n: ''.join([random.choice(string.ascii_lowercase) for i in xrange(n)])
		password = rand_str(8)
		self.instance.user.password = make_password(password)
		self.instance.user.save()
		print("swag")