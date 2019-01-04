from import_export import resources, fields, widgets
from rounds.models.assessments import Assessment, Rubric
from users.models import Judge, Team

class AssessmentResource(resources.ModelResource):

    round = fields.Field(column_name="Round")

    team = fields.Field(attribute="team",
        widget=widgets.ForeignKeyWidget(Team, 'number'),
        column_name="Team #")

    marks = fields.Field(column_name="Marks")

    total = fields.Field(column_name="Total Mark")

    judge = fields.Field(attribute="judge", column_name="Judge")

    class Meta:
        exclude = ('id', 'rough_notes', 'last_updated', 'submitted', 'rubric',)
        model = Assessment

    def dehydrate_round(self, assessment):
        return assessment.rubric.round.round_title()
    
    def dehydrate_marks(self, assessment):
        marks = list(assessment.marks.all())
        return ", ".join(
            [f"{mark.rubric_mark.title}: {str(mark.mark)}" for mark in marks]
        )
    
    def dehydrate_total(self, assessment):
        marks = list(assessment.marks.all())
        total = 0
        for mark in marks:
            total += mark.mark
        return total

    def dehydrate_judge(self, assessment):
        return (f"#{str(assessment.judge.number)}: " +
            f"{assessment.judge.user.get_full_name()}")