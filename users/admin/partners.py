# django modules
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# models
from users.models import User, Partner
# forms
from users.forms.partneradmin import (
	AdminPartnerUserCreationForm,
	AdminPartnerUserChangeForm,
)

class PartnerInline(admin.StackedInline):
	"""
	Inline group for partner model.
	"""
	model = Partner
	template = "admin/custom/stacked.html"
	verbose_name = "Partner Information"
	verbose_name_plural = "Partner Information"

class PartnerUser(User):
	"""
	Proxy for User, acting as a model of User.
	"""
	class Meta:
		proxy = True

@admin.register(PartnerUser)
class PartnerUserAdmin(UserAdmin):
	"""
	Add the fields in Partner on top of User, with specific form.
	"""
	# ADDING
	add_form_template = "admin/custom/add_partner_form.html"
	add_form = AdminPartnerUserCreationForm
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
	form = AdminPartnerUserChangeForm
	fieldsets = (
        (('CREDENTIALS'), {'fields': ('username', 'password')}),
        (('MAIN CONTACT'), {'fields': ('first_name', 'last_name', 'email')}),
        (('ACCOUNT META'), {'fields': ('last_login', 'date_joined',)}),
    )
	readonly_fields = ('date_joined', 'last_login',)
	# BOTH
	inlines = [PartnerInline]
	# LISTING
	list_display = ('company_name', 'partner_package',)
	list_filter = ()
	
	def company_name(self, x):
		"""
		Returns the company name of the partner.
		"""
		return x.partner.company_name

	def partner_package(self, x):
		"""
		Returns the package of the partner.
		"""
		return x.partner.partner_package

	def save_model(self, request, obj, form, change):
		"""
		When saving a model, ensure that it is saved as a partner.
		"""
		obj.is_delegate = False
		obj.is_partner = True
		obj.is_judge = False
		super().save_model(request, obj, form, change)

	def get_queryset(self, request):
		"""
		Returns a queryset where the user is a partner.
		"""
		return User.objects.filter(is_partner=True)