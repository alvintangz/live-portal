# Generated by Django 2.1.2 on 2018-11-28 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textnotification',
            name='title',
            field=models.CharField(default='Text at 2018-11-28 18:45:59.936871', max_length=100, verbose_name='title'),
        ),
    ]
