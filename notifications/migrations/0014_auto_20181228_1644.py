# Generated by Django 2.1.2 on 2018-12-28 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0013_auto_20181228_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textnotification',
            name='title',
            field=models.CharField(default='Text at 2018-12-28 16:44:51.428727', max_length=100, verbose_name='title'),
        ),
    ]
