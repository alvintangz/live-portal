from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from .models import Team, User, Delegate, Partner
from .forms.creation import AdminDelegateCreationForm

# Unregister Group that was automatically registered
admin.site.unregister(Group)

# Register Team
admin.site.register(Team)

# DELEGATES

class CustomUserAdmin(UserAdmin):
	add_form_template = "admin/custom/add_delegate_form.html"
	add_form = AdminDelegateCreationForm
	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('first_name', 
			'last_name', 
			'email', 
			'username', 
			'password1', 
			'password2',
			'autoemail',),
		}),
	)

class DelegateInline(admin.StackedInline):
	"""Inline group for delegate model."""
	template = "admin/custom/stacked.html"
	model = Delegate
	verbose_name = "Profile Information"
	verbose_name_plural = "Profile Information"
	fieldsets = (
		(None, {
            'fields': ('team', 'is_invisible')
        }),
		('Fields for Delegates to fill in', {
            'classes': ('collapse',),
            'fields': ('profile_picture',
				'school',
				'year_of_study',
				'program',
				'linkedin',
				'resume',
				'phone_number',
				'seeking_status'),
        }),
	)

class DelegateUser(User):
	"""Proxy for User, acting as a model of User."""
	class Meta:
		proxy = True

@admin.register(DelegateUser)
class DelegateUserAdmin(CustomUserAdmin):
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
	fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('PERSONAL INFO'), {'fields': ('first_name', 'last_name', 'email')}),
        (('ACCOUNT META'), {'fields': ('last_login', 'activated', 'agreed_terms')}),
    )

	readonly_fields = ('agreed_terms', )

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