# django modules
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# models
from users.models import User
# forms
from users.forms.administratoradmin import (
	AdminAdministratorUserCreationForm,
	AdminAdministratorUserChangeForm
)

class AdminUser(User):
	"""
	Proxy for User, acting as a model of User.
	"""
	class Meta:
		proxy = True
		verbose_name = "executive user"
		verbose_name_plural = "executive users"

@admin.register(AdminUser)
class DelegateUserAdmin(UserAdmin):
	"""
	Add the fields in Delegate on top of User, with specific form.
	"""
	# ADDING
	add_form_template = "admin/custom/add_administrator_form.html"
	add_form = AdminAdministratorUserCreationForm
	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('first_name', 
			'last_name', 
			'email', 
			'username', 
			'password1', 
			'password2',),
		}),
	)
	# CHANGING
	form = AdminAdministratorUserChangeForm
	fieldsets = (
        (('CREDENTIALS'), {'fields': ('username', 'password')}),
        (('PERSONAL INFO'), {'fields': ('first_name', 'last_name', 'email')}),
        (('ACCOUNT META'), {'fields': ('last_login', 'date_joined',)}),
    )
	readonly_fields = ('last_login', 'date_joined',)
	# LISTING
	list_display = (
		'first_name',
		'last_name',
        'email',
	)
	list_filter = ()

	def save_model(self, request, obj, form, change):
		"""
		When saving a model, ensure that it is saved with access.
		"""
		obj.is_delegate = False
		obj.is_partner = False
		obj.is_judge = False
		obj.is_staff = True
		obj.is_superuser = True
		super().save_model(request, obj, form, change)

	def get_queryset(self, request):
		"""
		Returns the queryset where the user is staff.
		"""
		return User.objects.filter(is_staff=True)