# Generated by Django 2.1.2 on 2018-12-27 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itenirary', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='venue_lat',
            field=models.DecimalField(decimal_places=6, default=0, help_text='The coordinates of the venue (latitude). Useful in maps. Can find coordinates using a tool: https://gps-coordinates.org/.', max_digits=9, verbose_name='venue latitude'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='venue_long',
            field=models.DecimalField(decimal_places=6, default=0, help_text='The coordinates of the venue (longitude). Useful in maps. Can find coordinates using a tool: https://gps-coordinates.org/.', max_digits=9, verbose_name='venue longitude'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(help_text='i.e. Registration', max_length=100, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='event',
            name='venue_address',
            field=models.CharField(help_text='i.e. 370 King St W, Toronto, ON M5V 1J9', max_length=200, verbose_name='venue address'),
        ),
        migrations.AlterField(
            model_name='event',
            name='venue_name',
            field=models.CharField(help_text='i.e. Hyatt Regency Toronto', max_length=100, verbose_name='venue name'),
        ),
    ]
