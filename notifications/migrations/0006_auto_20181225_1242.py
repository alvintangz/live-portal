# Generated by Django 2.1.2 on 2018-12-25 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0005_merge_20181223_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textnotification',
            name='title',
            field=models.CharField(default='Text at 2018-12-25 12:42:00.304913', max_length=100, verbose_name='title'),
        ),
    ]
