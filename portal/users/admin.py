from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Team, User, Delegate, Partner
from .forms import DelegateUserForm, PartnerUserForm

# Unregister Group that was automatically registered
admin.site.unregister(Group)

# Register Team
admin.site.register(Team)

# DELEGATES

# The inline group for delegate model
class DelegateInline(admin.StackedInline):
	model = Delegate

# The proxy for User, acting as a model of User
class DelegateUser(User):
	class Meta:
		proxy = True

# Where the magic begins, add the fields in Delegate on top of User, with specific form
@admin.register(DelegateUser)
class DelegateUserAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'email', 'get_team_number')
	inlines = [DelegateInline]
	form = DelegateUserForm

	def get_team_number(self, x):
		return x.delegate.team.number

	def get_queryset(self, request):
		return User.objects.filter(is_delegate=True).order_by('delegate__team__number')

# PARTNERS

# The inline group for partner model
class PartnerInline(admin.StackedInline):
	model = Partner

# The proxy for User, acting as a model of User
class PartnerUser(User):
	class Meta:
		proxy = True

# Where the magic begins, add the fields in Partner on top of User, with specific form
@admin.register(PartnerUser)
class PartnerUserAdmin(admin.ModelAdmin):
	list_display = ('get_company_name', 'get_partner_package')
	inlines = [PartnerInline]
	form = PartnerUserForm

	def get_company_name(self, x):
		return x.partner.company_name

	def get_partner_package(self, x):
		return x.partner.partner_package

	def get_queryset(self, request):
		return User.objects.filter(is_partner=True)

# OTHER USERS

# The proxy for User, acting as a model of User
class OtherUser(User):
	class Meta:
		proxy = True
		verbose_name = "other user"
		verbose_name_plural = "other users"

# Admin for Regular User (Not Partners/Delegates)
@admin.register(OtherUser)
class UserAdmin(admin.ModelAdmin):
	model = OtherUser

	def get_queryset(self, request):
		return User.objects.filter(is_partner=False).filter(is_delegate=False)