# django modules
from django.views.generic.edit import UpdateView
from django.shortcuts import redirect
# models
from rounds.models.assessments import Assessment
# helpers
from users.auth.mixins import JudgeRequiredMixin
from portal.functions import hashid_decode
from django.urls import reverse_lazy
# forms
from rounds.forms import AssessmentMarksFormSet

class AssessmentUpdateView(JudgeRequiredMixin, UpdateView):
	"""
	The view where judges assess a team's presentation and round.
	"""
	model = Assessment
	template_name = "rounds/judge.html"
	context_object_name = "ass"
	fields = ["rough_notes",]

	def get_success_url(self):
		"""
		Returns the success url for this view.
		"""
		return reverse_lazy('rounds-judge-listed-success',
			kwargs={"encoded":self.object.rubric.round.encoded_url})

	def dispatch(self, request, *args, **kwargs):
		"""
		Verify that the current judge user can view the specific round, and team
		based off the current object (assessment).
		"""
		if self.is_judge():
			if self.get_object().judge.pk == request.user.judge.pk:
				return super().dispatch(request, *args, **kwargs)
		return self.handle_no_permission()

	def get_context_data(self, **kwargs):
		"""
		The context provided to the template, with the assessment marks added
		as an inline formset using formset factory.
		"""
		context = super().get_context_data(**kwargs)
		if self.request.POST:
			context['ass_formset'] = AssessmentMarksFormSet(
				self.request.POST, instance=self.object)
			context['ass_formset'].full_clean()
		else:
			context['ass_formset'] = AssessmentMarksFormSet(
				instance=self.object)
		return context
	
	def form_valid(self, form):
		"""
		If the assessment form is valid, add validation for the assessment
		mark formset.
		"""
		context = self.get_context_data()
		formset = context['ass_formset']
		if formset.is_valid():
			self.object = form.save()
			formset.instance = self.object
			formset.save()
			self.object.submitted = True
			self.object.save()
			return redirect(self.get_success_url())
		return self.render_to_response(self.get_context_data(form=form))