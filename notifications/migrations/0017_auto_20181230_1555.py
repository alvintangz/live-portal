# Generated by Django 2.1.2 on 2018-12-30 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0016_auto_20181230_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textnotification',
            name='title',
            field=models.CharField(default='Text at 2018-12-30 15:55:28.911956', max_length=100, verbose_name='title'),
        ),
    ]
