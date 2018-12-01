# Generated by Django 2.1.2 on 2018-12-01 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CorporateIndividual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of', models.CharField(choices=[('Mentor', 'Mentor'), ('Judge', 'Judge'), ('Speaker', 'Speaker'), ('Networker', 'Networker')], max_length=10, verbose_name='type of individual')),
                ('position_org', models.CharField(max_length=100, verbose_name='position in their organization')),
                ('full_name', models.CharField(max_length=70, verbose_name='full name')),
                ('profile_picture', models.ImageField(blank=True, help_text='For best results, upload a 500px by 500px RGB picture. It will be resized and formatted automatically to that anyway.', null=True, upload_to='', verbose_name='picture')),
                ('biography', models.TextField(blank=True, help_text='Recommended to keep this short.', verbose_name='biography')),
                ('email', models.EmailField(blank=True, help_text='Optional.', max_length=254, verbose_name='Email')),
                ('linkedin', models.URLField(blank=True, help_text='Optional.', verbose_name='linkedin')),
                ('order', models.PositiveSmallIntegerField(help_text='Order an individual for when they are listed. i.e. If Bob has 1 for order of listing and Alice has 2 for order of listing, then Bob will be shown before Alice when listed.', verbose_name='order for listing')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='CorporateOrganization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='name')),
                ('description', models.TextField(blank=True, help_text='Optional.', verbose_name='description')),
                ('logo', models.ImageField(blank=True, help_text='<strong>It is highly recommended that a logo should be uploaded if they are a partner.</strong>', null=True, upload_to='', verbose_name='logo')),
                ('partner', models.BooleanField(default=False, help_text='If true, this organization will be viewable to delegates.', verbose_name='is a partner')),
                ('partner_type', models.SmallIntegerField(blank=True, choices=[(2, 'Silver Sponsor'), (3, 'Associate Sponsor'), (0, 'Finals Day'), (4, 'Prize Sponsor'), (1, 'Gold Sponsor'), (5, 'Swag Sponsor')], help_text='Leave blank if organization is not a partner. This is viewable to delegates if organization is a partner. As well, this will determine the ordering when partners listed.<br/>i.e. Title Partner', null=True, verbose_name='partner type')),
            ],
            options={
                'verbose_name': 'corporate organization',
                'ordering': ['partner_type'],
            },
        ),
        migrations.AddField(
            model_name='corporateindividual',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='individuals', to='corporate.CorporateOrganization'),
        ),
        migrations.CreateModel(
            name='Judge',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('corporate.corporateindividual',),
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('corporate.corporateindividual',),
        ),
        migrations.CreateModel(
            name='Networker',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('corporate.corporateindividual',),
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('corporate.corporateindividual',),
        ),
    ]
