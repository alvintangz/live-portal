# Generated by Django 2.1.2 on 2018-12-23 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0002_auto_20181222_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textnotification',
            name='title',
            field=models.CharField(default='Text at 2018-12-23 12:59:24.415037', max_length=100, verbose_name='title'),
        ),
    ]