# django modules
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect

def delegate_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME,
	login_url=None):
	"""Decorator to be used to check if logged in user is a delegate, and
	logged in. Otherwise, redirect user if they are not."""
	# Code similar to login_required in django.contrib.auth.decorators
	actual_decorator = user_passes_test(
		lambda u: (u.is_authenticated and u.is_delegate and u.activated),
		login_url=login_url,
		redirect_field_name=redirect_field_name
	)
	if function:
		return actual_decorator(function)
	return actual_decorator


def partner_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME,
	login_url=None):
	"""Decorator to be used to check if logged in user is a partner, and
	logged in. Otherwise, redirect user if they are not."""
	# Code similar to login_required in django.contrib.auth.decorators
	actual_decorator = user_passes_test(
		lambda u: (u.is_authenticated and u.is_partner and u.activated),
		login_url=login_url,
		redirect_field_name=redirect_field_name
	)
	if function:
		return actual_decorator(function)
	return actual_decorator