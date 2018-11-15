from django.shortcuts import render
from django.views.generic import ListView
from .models import Round, AcceptedRoundFile, Submission
from django.core.exceptions import ObjectDoesNotExist
from .forms import RoundUploadForm
from .constants.filetypes import FILETYPES
from users.views import viewByUser

# LISTED ROUNDS VIEW

# Get view depending on which user you are
def roundsListedView(request):
	return viewByUser(request, ListedRoundsView.as_view()(request), ListedRoundsView.as_view()(request))

# Generalized view for both delegates and partners
class ListedRoundsView(ListView):
	model = Round
	template_name = "rounds/rounds_listed.html"

	def get_queryset(self):
		return Round.objects.filter(visible=True).order_by("number")

# SPECIFIC ROUND VIEW

# Get view depending on which user you are
def roundsSpecificView(request, pk):
	return viewByUser(request, roundsSpecificView(request, pk), None)

def roundsSpecificView(request, pk):
	try:
		# Get the current round
		round = Round.object.get(pk=pk)
		# Empty context
		context = {}
		# All the submissions ordered by time submitted of the current user's team, and current round
		submissions = Submission.objects.filter(asc_team=team).filter(asc_round=round).order_by(submitted_at)
		# Puts the latest submissions in the context sent to the template
		context["submissions"] = list(submissions)
		# All the accepted round files
		accepted = AcceptedRoundFile.objects.filter(asc_round=round)
		context["accepted"] = dict()
		
		for each in accepted:
			context["accepted"][each] = RoundUploadForm(request.POST, request.FILES, each.get_validators())
		
		if request.method == 'POST':
			# assume true
			all_valid = True
			for each in accepted:
				if not (context["accepted"][each].is_valid() and all_valid):
					all_valid = False
				if all_valid:

	except ObjectDoesNotExist:
		context= {"dne": True}

	return render(request, 'users/delegate/edit_profile.html', context)