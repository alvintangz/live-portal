from django.contrib import admin
from rounds.models.assessments import (
    Rubric,
    RubricMark,
    Assessment,
    AssessmentMark
)
from users.models import Judge, User, Team
# import export
from import_export.admin import ExportActionModelAdmin
from rounds.resources import AssessmentResource

class RubricMarkInline(admin.StackedInline):
    model = RubricMark
    extra = 1

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(Rubric)
class RubricAdmin(admin.ModelAdmin):
    inlines = (RubricMarkInline,)
    list_display = ('get_round_name',)
    ordering = ('round__number',)

    def get_round_name(self, request):
        return request.round.__str__()
    get_round_name.short_description = "Round name"

class AssessmentMarkInline(admin.StackedInline):
    model = AssessmentMark
    extra = 0
    exclude = ('rubric_mark',)

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(Assessment)
class AssessmentAdmin(ExportActionModelAdmin):
    resource_class = AssessmentResource
    inlines = (AssessmentMarkInline,)
    ordering = ('rubric', 'team', 'submitted',)
    list_display = ('judge', 'rubric', 'team', 'submitted',)
    list_filter = ('judge', 'rubric', 'team', 'submitted',)
    readonly_fields = ('rubric', 'team', 'judge', 'rough_notes','submitted')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

# Selecting Assessments for Judges

class AssessmentInline(admin.StackedInline):
    model = Assessment
    extra = 1
    add_fieldsets = (
        ((), {'fields': ('rubric', 'team',)}),
    )
    fieldsets = (
        ((), {'fields': ('rubric', 'team', 'submitted',)}),
    )
    readonly_fields = ('submitted',)

    def get_fieldsets(self, request, obj=None):
        if obj:
            return self.fieldsets
        return self.add_fieldsets

class JudgeAssessments(Judge):
	"""
	Proxy for Judge, acting as a model of Judge.
	"""
	class Meta:
		proxy = True
		verbose_name = "Assign assessments for Judges"
		verbose_name_plural = "Assign assessments for Judges"

@admin.register(JudgeAssessments)
class JudgeAdmin(admin.ModelAdmin):
    inlines = [AssessmentInline]
    exclude = ('number', 'room',)
    list_display = ('__str__', 'get_assessments')

    def has_delete_permission(self, request, obj=None):
        return False

    def render_change_form(self, request, context, *args, **kwargs):
        context['adminform'].form.fields['user'].queryset = User.objects.filter(
            is_judge=True)
        return super().render_change_form(request, context, *args, **kwargs)