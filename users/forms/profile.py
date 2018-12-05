# django modules
from django.core.validators import FileExtensionValidator
from django.core.validators import FileExtensionValidator
from django.template.defaultfilters import filesizeformat
from django import forms
# models
from users.models import Delegate
# helpers
import re

MAX_UPLOAD_SIZE = 1

class DelegateProfileUpdateForm(forms.ModelForm):
	"""A form with basic delegate information."""
	first_name = forms.CharField(max_length=30)
	last_name = forms.CharField(max_length=30)
	linkedin = forms.URLField(required=False)
	profile_picture = forms.FileField(required=False, validators=[
		FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])
	resume = forms.FileField(validators=[FileExtensionValidator(
		allowed_extensions=['pdf'])])

	class Meta:
		model = Delegate
		fields = ['profile_picture', 'year_of_study', 'school', 'program', 
		'linkedin', 'resume', 'phone_number', 'seeking_status']

	def __init__(self, *args, **kw):
		super(DelegateProfileUpdateForm, self).__init__(*args, **kw)
		self.fields['first_name'].initial = self.instance.user.first_name
		self.fields['last_name'].initial = self.instance.user.last_name
		self.fields["school"].widget.attrs["class"] = "form-control"
		self.fields["year_of_study"].widget.attrs["class"] = "form-control"
		self.fields["seeking_status"].widget.attrs["class"] = "form-control"

	def is_valid(self):
		valid = super(DelegateProfileUpdateForm, self).is_valid()

		# Return if not valid anyways
		if not valid:
			return valid

		# ADD FILE FORM VALIDATION

		# If linkedin profile is not blank
		if self.cleaned_data['linkedin'] != "":
			# Regex from: https://bit.ly/2zY11AG
			regex = "^https:\\/\\/[a-z]{2,3}\\.linkedin\\.com\\/.*$"
			if not re.match(regex, self.cleaned_data['linkedin']):
				return False

		# If phone number is not blank
		if self.cleaned_data['phone_number'] != "":
			try:
				num = int(self.cleaned_data['phone_number'])
				if not len(str(num)) == 10:
					return not valid
			except ValueError:
				return False

		# Just return valid
		return valid

	def save(self):
		instance = super(DelegateProfileUpdateForm, self).save()
		self.instance.user.first_name = self.cleaned_data["first_name"]
		self.instance.user.last_name = self.cleaned_data["last_name"]
		self.instance.user.save()