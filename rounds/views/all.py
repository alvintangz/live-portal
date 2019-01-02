from django.contrib.auth.decorators import login_required
from users.auth.decorators import delegate_required
from .listed import ListedRoundsView
from .upload import UploadRoundsView

def roundsListedView(request):
	"""View for looking at a list of rounds."""
	return ListedRoundsView.as_view()(request)

@delegate_required
def roundsUploadView(request, encoded):
	"""View for looking at a specific round."""
	return UploadRoundsView.as_view()(request, encoded)