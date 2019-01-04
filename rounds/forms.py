# django modules
from django import forms
from django.forms.models import inlineformset_factory
from django.core.validators import FileExtensionValidator
from django.template.defaultfilters import filesizeformat
from django.conf import settings
# models
from rounds.models.rounds import Round, AcceptedRoundFile
from rounds.models.submissions import Submission
from rounds.models.assessments import Assessment, AssessmentMark, RubricMark
# constants
from rounds.constants.filetypes import FILETYPES
# helpers
import datetime

MAX_UPLOAD_SIZE = 10485760

class RoundUploadForm(forms.ModelForm):
	class Meta:
		model = Round
		fields = ()

	def __init__(self, *args, **kwargs):
		team = kwargs.pop('team', None)
		super(RoundUploadForm, self).__init__(*args, **kwargs)
		accepted_files = AcceptedRoundFile.objects.filter(
			asc_round=self.instance)
		for accepted in accepted_files:
			self.fields["upload_%d" % accepted.pk] = forms.FileField(
				validators=[FileExtensionValidator(
					accepted.get_validators())],
				help_text=accepted.get_validators_str(),
				label=accepted.get_title_for_delegates())

			submission_count = Submission.objects.filter(
				asc_team=team).filter(
				asc_round_file=accepted).count()
			if submission_count > 0:
				self.fields["upload_%d" % accepted.pk].required = False
			else:
				self.fields["upload_%d" % accepted.pk].required = True
				self.fields["upload_%d" % accepted.pk].widget.attrs["required"
				] = "required"
				self.fields["upload_%d" % accepted.pk
				].label += ' *'

			self.fields["upload_%d" % accepted.pk].widget.attrs["class"
			] = "form-control"

			self.fields["upload_%d" % accepted.pk].widget.attrs["accept"
			] = accepted.get_validators_accepted_html()

	def is_valid(self):
		valid = super(RoundUploadForm, self).is_valid()

		for field_name, field_value in self.cleaned_data.items():
			if bool(field_value) is True:
				if field_value.size > MAX_UPLOAD_SIZE:
					self.add_error(field_name, 
						('Please keep filesize under %s. Current filesize is %s') 
						% (filesizeformat(MAX_UPLOAD_SIZE), 
						filesizeformat(field_value.size)))
					#raise forms.ValidationError(
					#	('Please keep filesize under %s. Current filesize %s') 
					#		% (filesizeformat(MAX_UPLOAD_SIZE), 
					#		filesizeformat(field_value.size)))
					return False
				return valid

		return False

	def save(self, commit=True, *args, **kwargs):
		team = kwargs.pop('team', None)
		user_id = kwargs.pop('user_id', None)
		super(RoundUploadForm, self).save(commit=False)
		if self.instance.active:
			for field_name, field_value in self.cleaned_data.items():
				if field_name.startswith("upload_"):
					if bool(field_value) is True:
						a_id = int(field_name.split("_")[1])
						accepted = AcceptedRoundFile.objects.get(pk=a_id)
						Submission.objects.filter(asc_team=team).filter(
						asc_round_file=accepted).update(latest=False)
						new_submission = Submission.objects.create(
							asc_team=team,
							asc_round_file=accepted,
							asc_round=accepted.asc_round,
							submitted_by=user_id,
							submitted_file=field_value,
							submitted_at=datetime.datetime.now(),
							latest=True)
						new_submission.save()
		return True

class AssessmentMarkForm(forms.ModelForm):
	class Meta:
		model = AssessmentMark
		fields = ('mark',)
		exclude = ('rubric_mark',)

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		max_mark = self.instance.rubric_mark.max_mark
		mark_title = self.instance.rubric_mark.title
		self.fields["mark"].label = (
			f"{mark_title} (out of {str(max_mark)})")
		self.fields["mark"].required = True
		self.fields["mark"].widget.attrs["class"] = "form-control"
		self.fields["mark"].widget.attrs["min"] = "0"
		self.fields["mark"].widget.attrs["max"] = str(max_mark)
		self.fields["mark"].widget.attrs["onkeyup"] = "mlc(this)"
		self.fields["mark"].widget.attrs["placeholder"] = "__/" + str(max_mark)

AssessmentMarksFormSet = inlineformset_factory(Assessment, 
	AssessmentMark,
	extra=0,
	can_delete=False,
	fields=('mark',),
	form=AssessmentMarkForm)