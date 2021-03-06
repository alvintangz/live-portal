# Generated by Django 2.1.2 on 2019-01-03 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rounds', '0009_assessment_submitted'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='judgeassessments',
            options={'verbose_name': 'Assign assessments for Judges', 'verbose_name_plural': 'Assign assessments for Judges'},
        ),
        migrations.AlterField(
            model_name='assessmentmark',
            name='assessment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='marks', to='rounds.Assessment', verbose_name='assessment'),
        ),
        migrations.AlterField(
            model_name='assessmentmark',
            name='mark',
            field=models.PositiveSmallIntegerField(help_text='The assessment mark cannot be greater than the rubric mark.', null=True, verbose_name='assessment mark'),
        ),
        migrations.AlterField(
            model_name='round',
            name='visible',
            field=models.BooleanField(default=False, help_text='If True, all parties can view the details of the round.', verbose_name='visible'),
        ),
        migrations.AlterField(
            model_name='rubric',
            name='release',
            field=models.BooleanField(default=True, help_text='If this is True, then the round is visible to judge.', verbose_name='release rubric'),
        ),
        migrations.AlterField(
            model_name='rubricmark',
            name='rubric',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='marks', to='rounds.Rubric', verbose_name='rubric'),
        ),
    ]
