# Generated by Django 2.1.2 on 2018-12-30 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qanda', '0002_auto_20181218_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='faq',
            field=models.BooleanField(default=False, help_text='If True, the answer and its associated question will be appended to a special FAQ section.', verbose_name='is frequently asked'),
        ),
    ]
