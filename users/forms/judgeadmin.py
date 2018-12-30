# django modules
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User
from django import forms

class AdminJudgeCreationForm(UserCreationForm):

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        # self.fields["number"].value = "1"

    def save(self, commit=True):
        user = super().save(commit=True)
        user.activated = True
        return user