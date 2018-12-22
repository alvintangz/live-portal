# Generated by Django 2.1.2 on 2018-12-21 22:14

from django.db import migrations, models
import users.helpers


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delegate',
            name='profile_picture',
            field=models.ImageField(blank=True, max_length=500, upload_to=users.helpers.profile_picture_upload_to, verbose_name='profile picture'),
        ),
    ]
