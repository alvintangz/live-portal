from django.core.validators import FileExtensionValidator
from django import forms
from users.models import Delegate
from portal.functions import send_email, send_sms
import portal.variables as imp
import re
import datetime

class EmailForm(forms.Form):
	delegate_name = forms.CharField(label="Delegate Name")
	delegate_email = forms.EmailField(label="Delegate Email")
	activation_link = forms.URLField(label="Activation Link")
	username = forms.CharField(label="Username of Delegate")
	password = forms.CharField(label="Password of Delegate")

	def save(self):
		send_email(subject="Acceptance: Access to Portal & Preliminaries ",
			receiver=self.cleaned_data["delegate_email"],
			message=((imp.email_messages["delegate_creation"]["plain"])
			 % (self.cleaned_data["delegate_name"],
			 	self.cleaned_data["activation_link"],
			 	self.cleaned_data["username"],
			 	self.cleaned_data["password"])),
			html_message=((imp.email_messages["delegate_creation"]["html"])
			 % (self.cleaned_data["delegate_name"],
			 	self.cleaned_data["activation_link"],
			 	self.cleaned_data["activation_link"],
			 	self.cleaned_data["username"],
			 	self.cleaned_data["password"])))

class ConfirmDelegateForm(forms.ModelForm):
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
		super(ConfirmDelegateForm, self).__init__(*args, **kw)
		self.fields['first_name'].initial = self.instance.user.first_name
		self.fields['last_name'].initial = self.instance.user.last_name
		self.fields["school"].widget.attrs["class"] = "form-control"
		self.fields["year_of_study"].widget.attrs["class"] = "form-control"
		self.fields["seeking_status"].widget.attrs["class"] = "form-control"

	def is_valid(self):
		valid = super(ConfirmDelegateForm, self).is_valid()

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
		instance = super(ConfirmDelegateForm, self).save()
		self.instance.user.first_name = self.cleaned_data["first_name"]
		self.instance.user.last_name = self.cleaned_data["last_name"]
		self.instance.user.activated = True
		self.instance.agreed_terms = datetime.datetime.now()
		send_email(subject="LIVE Portal: Account Activated",
			receiver=self.instance.user.email,
			message=((imp.email_messages["delegate_activation"]["plain"])
			 % (self.instance.user.first_name)),
			html_message=((imp.email_messages["delegate_activation"]["html"])
			 % (self.instance.user.first_name)))
		if self.instance.phone_number:
			send_sms("+1"+self.instance.phone_number,
				imp.sms_messages["delegate_activation"])
		self.instance.user.save()