# Generated by Django 2.1.2 on 2018-12-30 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0015_auto_20181230_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textnotification',
            name='title',
            field=models.CharField(default='Text at 2018-12-30 13:57:35.273375', max_length=100, verbose_name='title'),
        ),
    ]