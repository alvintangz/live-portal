from django.contrib.auth.decorators import login_required
from users.functions import viewByUser
from .listed import ListedRoundsView
from .upload import UploadRoundsView

def roundsListedView(request):
	"""View for looking at a list of rounds."""
	return viewByUser(request, 
		ListedRoundsView.as_view()(request),
		ListedRoundsView.as_view()(request))

def roundsUploadView(request, encoded):
	"""View for looking at a specific round."""
	return viewByUser(request,
		UploadRoundsView.as_view()(request, encoded),
		None)