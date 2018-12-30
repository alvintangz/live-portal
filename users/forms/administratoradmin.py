# django modules
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms

class AdminAdministratorUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kw):
        super(AdminAdministratorUserCreationForm, self).__init__(*args, **kw)
        self.fields['email'].required = True

    def save(self, commit=True):
        """
        On save, set the activated field to True.
        """
        user = super().save(commit=True)
        user.activated = True
        return user

class AdminAdministratorUserChangeForm(UserChangeForm):
    def __init__(self, *args, **kw):
        super(AdminAdministratorUserChangeForm, self).__init__(*args, **kw)
        self.fields['email'].required = True