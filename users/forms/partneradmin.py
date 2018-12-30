# django modules
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms

class AdminPartnerUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kw):
        super(AdminPartnerUserCreationForm, self).__init__(*args, **kw)
        self.fields['email'].required = True
        mcht = "Enter the %s of the main contact for this partner."
        self.fields['first_name'].help_text = mcht % ("first name")
        self.fields['last_name'].help_text = mcht % ("last name")
        self.fields['email'].help_text = mcht % ("email")

    def save(self, commit=True):
        """
        On save, set the activated field to True.
        """
        user = super().save(commit=True)
        user.activated = True
        return user

class AdminPartnerUserChangeForm(UserChangeForm):
    def __init__(self, *args, **kw):
        super(AdminPartnerUserChangeForm, self).__init__(*args, **kw)
        self.fields['email'].required = True
        mcht = "Enter the %s of the main contact for this partner."
        self.fields['first_name'].help_text = mcht % ("first name")
        self.fields['last_name'].help_text = mcht % ("last name")
        self.fields['email'].help_text = mcht % ("email")