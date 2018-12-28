from django.contrib import admin
from rounds.models.assessments import (
    Rubric,
    RubricMark,
    Assessment,
    AssessmentMark
)

class RubricMarkInline(admin.StackedInline):
    model = RubricMark
    extra = 1

@admin.register(Rubric)
class Rubric(admin.ModelAdmin):
    inlines = (RubricMarkInline,)

class AssessmentMarkInline(admin.StackedInline):
    model = AssessmentMark
    extra = 1

@admin.register(Assessment)
class Assessment(admin.ModelAdmin):
    inlines = (AssessmentMarkInline,)
    list_display = ('judge', 'rubric', 'team',)
    list_filter = ('judge', 'rubric', 'team',)