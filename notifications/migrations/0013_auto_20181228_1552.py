# Generated by Django 2.1.2 on 2018-12-28 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0012_auto_20181227_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textnotification',
            name='title',
            field=models.CharField(default='Text at 2018-12-28 15:52:11.136599', max_length=100, verbose_name='title'),
        ),
    ]
