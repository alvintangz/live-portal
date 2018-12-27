# Generated by Django 2.1.2 on 2018-12-27 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('itenirary', '0003_auto_20181227_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='day',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='day', to='itenirary.Day'),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.TimeField(help_text='When the event ends. Not displayed.', verbose_name='end time'),
        ),
    ]