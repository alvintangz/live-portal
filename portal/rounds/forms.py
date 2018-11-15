from django import forms
from django.core.validators import FileExtensionValidator
from .models import Round, AcceptedRoundFile

class RoundUploadForm(forms.ModelForm, validators):
	file = forms.FileField(validators=[FileExtensionValidator(allowed_extensions=validators)