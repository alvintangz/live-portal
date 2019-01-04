# django modules
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# models
from django.contrib.auth.models import Group
from users.models import Team, User

# Unregister Group that was automatically registered
admin.site.unregister(Group)

# Register Team
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    ordering = ('number',)