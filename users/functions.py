# django modules
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

@login_required
def viewByUser(request, delegateView=None, partnerView=None, judgeView=None, redi='sign-in'):
	"""Return a view based off which type of user is logged in."""
	
	http_response = redirect(redi)
	
	if not request.user.is_anonymous and request.user.activated:
		if hasattr(request.user, 'delegate'):
			if request.user.is_delegate:
				if delegateView is None:
					http_response = redirect(redi)
				else:
					http_response = delegateView
		elif hasattr(request.user, 'partner'):
			if request.user.is_partner:
				if partnerView is None:
					http_response = redirect(redi)
				else:
					http_response = partnerView
		elif hasattr(request.user, 'judge'):
			if request.user.is_judge:
				if judgeView is None:
					http_response = redirect(redi)
				else:
					http_response = judgeView

	return http_response