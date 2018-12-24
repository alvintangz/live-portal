# django modules
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User
from django import forms
# helpers
import portal.variables as imp
from portal.functions import send_email

class AdminDelegateCreationForm(UserCreationForm):

    autoemail = forms.BooleanField(
        label="Automatically send email",
        initial=True,
        help_text="Automatically email the delegate to activate account.",
        required=False
    )

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.fields["email"].widget.attrs["onkeyup"] = "eAUS()"

    def save(self, commit=True):
        user = super().save(commit=True)
        if self.cleaned_data['autoemail']:
            send_email(subject="Access to Portal: Preliminary Submission",
			receiver=self.cleaned_data["email"],
			message=((imp.email_messages["delegate_creation"]["plain"])
			 % (self.cleaned_data["first_name"],
			 	user.activation_link(),
			 	self.cleaned_data["username"],
			 	self.cleaned_data["password1"])),
			html_message=((imp.email_messages["delegate_creation"]["html"])
			 % (self.cleaned_data["first_name"],
			 	user.activation_link(),
			 	user.activation_link(),
			 	self.cleaned_data["username"],
			 	self.cleaned_data["password1"])))
        return user

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name' , 'last_name', 'email',)