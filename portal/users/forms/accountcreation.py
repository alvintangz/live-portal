# from users.constants.universities import CANADIAN_UNIS
# from users.constants.student_types import STUDENT_TYPES
# from users.constants.seeking_statuses import SEEKING_STATUSES
# from django.contrib.auth.hashers import make_password
# from django import forms
# from users.models import Delegate, Team
# from users.helpers import resume_upload_to
# import re

# def generate_username(first, last):
# 	users = User.objects.all()
# 	counter = 1
# 	good = False
# 	while(not good):
# 		username = (first + last)[:8] + counter
# 		good = True
# 		for user in users:
# 			if username == user.username:
# 				good = False
# 		counter += 1
# 	return username

# class DelegateCreateForm(forms.Form):
# 	"""A form with basic delegate information."""
# 	first_name = forms.CharField(max_length=30)
# 	last_name = forms.CharField(max_length=30)
# 	email = forms.EmailField()
# 	year_of_study = forms.ChoiceField(choices=STUDENT_TYPES)
# 	school = forms.ChoiceField(choices=CANADIAN_UNIS)
# 	program = forms.CharField(max_length=150)
# 	linkedin = forms.URLField(max_length=100)
# 	resume = forms.FileField(upload_to=resume_upload_to)
# 	phone_number = forms.CharField(max_length=10)
# 	team = forms.ModelChoiceField(queryset=Team.objects.all())
# 	seeking_status = forms.ChoiceField(choices=SEEKING_STATUSES)

# 	def is_valid(self):
# 		valid = super(DelegateCreateForm, self).is_valid()

# 		# Return if not valid anyways
# 		if not valid:
# 			return valid

# 		# If linkedin profile is not blank
# 		if self.cleaned_data['linkedin'] != "":
# 			# Regex from: https://bit.ly/2zY11AG
# 			regex = "^https:\\/\\/[a-z]{2,3}\\.linkedin\\.com\\/.*$"
# 			if not re.match(regex, self.cleaned_data['linkedin']):
# 				return not valid

# 		# If phone number is not blank
# 		if self.cleaned_data['phone_number'] != "":
# 			try:
# 				num = int(self.cleaned_data['phone_number'])
# 				if not len(str(num)) == 10:
# 					return not valid
# 			except ValueError:
# 				return not valid

# 		# Just return valid
# 		return valid

# 	def save(self):
# 		instance = super
# 		instance = super(DelegateCreateForm, self).save()
# 		self.instance.user.first_name = self.cleaned_data["first_name"]
# 		self.instance.user.last_name = self.cleaned_data["last_name"]
# 		self.instance.user.email = self.cleaned_data["email"]
# 		self.instance.user.username = generate_username(self.cleaned_data["first_name"], self.cleaned_data["last_name"])
# 		rand_str = lambda n: ''.join([random.choice(string.ascii_lowercase) for i in xrange(n)])
# 		password = rand_str(8)
# 		self.instance.user.password = make_password(password)
# 		self.instance.user.save()
# 		print("swag")