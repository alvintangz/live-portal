from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from .models import Team, User, Delegate, Partner

# Unregister Group that was automatically registered
admin.site.unregister(Group)

# Register Team
admin.site.register(Team)

# DELEGATES

class DelegateInline(admin.StackedInline):
	"""Inline group for delegate model."""
	model = Delegate

class DelegateUser(User):
	"""Proxy for User, acting as a model of User."""
	class Meta:
		proxy = True

@admin.register(DelegateUser)
class DelegateUserAdmin(UserAdmin, ImportExportModelAdmin):
	"""Add the fields in Delegate on top of User, with specific form."""
	list_display = (
		'first_name',
		'last_name',
		'email',
		'team_number',
		'activation_link',
		'activated'
	)
	list_filter = ()
	inlines = [DelegateInline]

	def team_number(self, x):
		"""Returns the team number of the user."""
		return x.delegate.team.number

	def save_model(self, request, obj, form, change):
		"""When saving a model, ensure that it is saved as a delegate."""
		obj.is_delegate = True
		obj.is_partner = False
		super().save_model(request, obj, form, change)

	def get_queryset(self, request):
		"""Returns the queryset where the user is a delegate, ordered by team
		number."""
		return User.objects.filter(is_delegate=True
			).order_by('delegate__team__number')

DelegateUserAdmin.fieldsets += (('Activated',{'fields': ('activated','agreed_terms')}),)

# PARTNERS

class PartnerInline(admin.StackedInline):
	"""Inline group for partner model."""
	model = Partner

class PartnerUser(User):
	"""Proxy for User, acting as a model of User"""
	class Meta:
		proxy = True

@admin.register(PartnerUser)
class PartnerUserAdmin(UserAdmin):
	"""Add the fields in Partner on top of User, with specific form."""
	list_display = ('company_name', 'partner_package')
	list_filter = ()
	inlines = [PartnerInline]

	def company_name(self, x):
		"""Returns the company name of the partner."""
		return x.partner.company_name

	def partner_package(self, x):
		"""Returns the package of the partner."""
		return x.partner.partner_package

	def save_model(self, request, obj, form, change):
		"""When saving a model, ensure that it is saved as a partner."""
		obj.is_delegate = False
		obj.is_partner = True
		super().save_model(request, obj, form, change)

	def get_queryset(self, request):
		"""Returns a queryset where the user is a partner."""
		return User.objects.filter(is_partner=True)

# OTHER USERS

class OtherUser(User):
	"""Proxy for User, acting as a model of User."""
	class Meta:
		proxy = True
		verbose_name = "other user"
		verbose_name_plural = "other users"

@admin.register(OtherUser)
class OtherUserAdmin(UserAdmin):
	"""Admin for Regular User (Not Partners/Delegates)"""
	model = OtherUser
	list_filter = ()

	def get_queryset(self, request):
		"""Returns a queryset where a user is neither a partner nor delegate.
		"""
		return User.objects.filter(is_partner=False).filter(is_delegate=False)

# Comment out during production
admin.site.register(User)