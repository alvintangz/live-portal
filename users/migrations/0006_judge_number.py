# Generated by Django 2.1.2 on 2018-12-28 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_judgeuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='judge',
            name='number',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='number'),
            preserve_default=False,
        ),
    ]