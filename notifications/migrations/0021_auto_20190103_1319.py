# Generated by Django 2.1.2 on 2019-01-03 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0020_auto_20190103_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textnotification',
            name='title',
            field=models.CharField(default='Text at 2019-01-03 13:19:18.472810', max_length=100, verbose_name='title'),
        ),
    ]
