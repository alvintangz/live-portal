# django modules
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# models
from users.models import User, Judge
# forms
from users.forms.judgeadmin import AdminJudgeCreationForm

class JudgeInline(admin.StackedInline):
	"""
	Inline group for judge model.
	"""
	model = Judge
	template = "admin/custom/stacked_nt.html"
	fieldsets = (
		(None, {
            'fields': ('number',
				'room')
        }),
	)

class JudgeUser(User):
	"""
	Proxy for User, acting as a model of Judge.
	"""
	class Meta:
		proxy = True

@admin.register(JudgeUser)
class JudgeUserAdmin(UserAdmin):
	"""
	Add the fields in Judge on top of User, with specific form.
	"""
	# ADDING
	add_form_template = "admin/custom/add_judge_form.html"
	add_form = AdminJudgeCreationForm
	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('first_name',
			'last_name',
			'username',
			'password1', 
			'password2',),
		}),
	)
	# CHANGING
	fieldsets = (
        (('CREDENTIALS'), {'fields': ('username', 'password')}),
        (('PERSONAL INFO'), {'fields': ('first_name', 'last_name',)}),
        (('ACCOUNT META'), {'fields': ('last_login',)}),
    )
	readonly_fields = ()
	# BOTH
	inlines = [JudgeInline]
	# LISTING
	list_display = ('username',)
	list_filter = ()

	def save_model(self, request, obj, form, change):
		"""
		When saving a model, ensure that it is saved as a judge.
		"""
		obj.is_delegate = False
		obj.is_partner = False
		obj.is_judge = True
		super().save_model(request, obj, form, change)

	def get_queryset(self, request):
		"""
		Returns a queryset where the user is a judge.
		"""
		return User.objects.filter(is_judge=True)