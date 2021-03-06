# Generated by Django 2.1.2 on 2018-12-27 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corporate', '0009_auto_20181227_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='corporateorganization',
            name='partner_type',
            field=models.SmallIntegerField(blank=True, choices=[(4, 'Prize Sponsor'), (1, 'Gold Sponsor'), (3, 'Associate Sponsor'), (2, 'Silver Sponsor'), (5, 'Swag Sponsor'), (0, 'Finals Day')], help_text='Leave blank if organization is not a partner. This is viewable to delegates if organization is a partner. As well, this will determine the ordering when partners listed.<br/>i.e. Title Partner', null=True, verbose_name='partner type'),
        ),
    ]
