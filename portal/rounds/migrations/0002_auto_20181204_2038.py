# Generated by Django 2.1.2 on 2018-12-04 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('rounds', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='asc_team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.Team'),
        ),
        migrations.AddField(
            model_name='acceptedroundfile',
            name='asc_round',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rounds.Round'),
        ),
    ]