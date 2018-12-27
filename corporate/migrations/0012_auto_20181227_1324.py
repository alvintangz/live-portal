# Generated by Django 2.1.2 on 2018-12-27 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corporate', '0011_auto_20181227_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='corporateorganization',
            name='partner_type',
            field=models.SmallIntegerField(blank=True, choices=[(5, 'Swag Sponsor'), (3, 'Associate Sponsor'), (0, 'Finals Day'), (1, 'Gold Sponsor'), (4, 'Prize Sponsor'), (2, 'Silver Sponsor')], help_text='Leave blank if organization is not a partner. This is viewable to delegates if organization is a partner. As well, this will determine the ordering when partners listed.<br/>i.e. Title Partner', null=True, verbose_name='partner type'),
        ),
    ]
