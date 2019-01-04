# django modules
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# models
from users.models import User, Delegate
# forms
from users.forms.delegateadmin import (
	AdminDelegateUserCreationForm,
	AdminDelegateUserChangeForm
)

class DelegateInline(admin.StackedInline):
	"""
	Inline group for delegate model.
	"""
	model = Delegate
	template = "admin/custom/stacked.html"
	verbose_name = "Profile Information"
	verbose_name_plural = "Profile Information"
	fieldsets = (
		(None, {
            'fields': ('team', 'is_invisible', 'profile_picture_block')
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
	"""
	Proxy for User, acting as a model of User.
	"""
	class Meta:
		proxy = True

@admin.register(DelegateUser)
class DelegateUserAdmin(UserAdmin):
	"""
	Add the fields in Delegate on top of User, with specific form.
	"""
	# ADDING
	add_form_template = "admin/custom/add_delegate_form.html"
	add_form = AdminDelegateUserCreationForm
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
	# CHANGING
	form = AdminDelegateUserChangeForm
	fieldsets = (
        (('CREDENTIALS'), {'fields': ('username', 'password')}),
        (('PERSONAL INFO'), {'fields': ('first_name', 'last_name', 'email')}),
        (('ACCOUNT META'), {'fields': ('last_login', 'date_joined', 'activated', 
			'agreed_terms', 'activation_link')}),
    )
	readonly_fields = ('agreed_terms', 'last_login', 'date_joined', 
		'activation_link',)
	# BOTH
	inlines = [DelegateInline]
	# LISTING
	list_display = (
		'first_name',
		'last_name',
		'email',
		'team_number',
		'activated'
	)
	list_filter = ('activated', 'delegate__team__number',)
	ordering = ('delegate__team__number', '-activated',)
	
	def team_number(self, x):
		"""
		Returns the team number of the user.
		"""
		return x.delegate.team.number

	def save_model(self, request, obj, form, change):
		"""
		When saving a model, ensure that it is saved as a delegate.
		"""
		obj.is_delegate = True
		obj.is_partner = False
		obj.is_judge = False
		super().save_model(request, obj, form, change)

	def get_queryset(self, request):
		"""
		Returns the queryset where the user is a delegate.
		"""
		return User.objects.filter(is_delegate=True)