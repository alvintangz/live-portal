from django.contrib import admin
from django import forms
from django.contrib.auth.models import Group
from .models import Team, User, Delegate, Partner

admin.site.unregister(Group)
admin.site.register(Team)

# Admin for Delegate User
class DelegateInline(admin.StackedInline):
	model = Delegate

class DelegateUser(User):
	class Meta:
		proxy = True

class DelegateUserForm(forms.ModelForm):
	class Meta:
		model = User
		exclude = ['is_partner', 'is_delegate', 'is_superuser', 'is_staff', 'groups', 'user_permissions', 'last_login', 'email']

	def save(self, commit=True):
		user = super(DelegateUserForm, self).save(commit=False)
		if(user.check_password(self.cleaned_data["password"])):
			user.set_password(self.cleaned_data["password"])
		user.set_delegate()
		user.set_email(self.cleaned_data["username"])
		if commit:
			user.save()
		return user

class DelegateUserAdmin(admin.ModelAdmin):
	inlines = [DelegateInline]
	form = DelegateUserForm

	def get_queryset(self, request):
		return User.objects.filter(is_delegate=True)

admin.site.register(DelegateUser, DelegateUserAdmin)

# Admin for Partner User
class PartnerInline(admin.StackedInline):
	model = Partner

class PartnerUser(User):
	class Meta:
		proxy = True

class PartnerUserAdmin(admin.ModelAdmin):
	inlines = [PartnerInline]

	def get_queryset(self, request):
		return User.objects.filter(is_partner=True)

admin.site.register(PartnerUser, PartnerUserAdmin)

# Admin for Regular User (Not Partner/Delegate)
class UserAdmin(admin.ModelAdmin):
	model = User

	def get_queryset(self, request):
		return User.objects.filter(is_partner=False).filter(is_delegate=False)

	class Meta:
		verbose_name = "other user"
		verbose_name_plural = "other users"

admin.site.register(User, UserAdmin)