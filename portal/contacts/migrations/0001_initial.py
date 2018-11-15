# Generated by Django 2.1.2 on 2018-11-13 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position_title', models.IntegerField(choices=[(1, 'President'), (2, 'Vice President of Corporate Relations'), (3, 'Corporate Relations Manager'), (4, 'Vice President of Operations'), (5, 'Delegate Experience Manager'), (6, 'Vice President of Curriculum'), (7, 'Curriculum Manager'), (8, 'Vice President of Business Intelligence'), (9, 'Business Analyst'), (10, 'Vice President of Marketing'), (11, 'Marketing Manager'), (12, 'External Relations Manager'), (13, 'Information Technology Solutions Manager'), (14, 'Board Member')], verbose_name='position')),
                ('show_delegates', models.BooleanField(default=True, verbose_name='viewable to delegates')),
                ('show_partners', models.BooleanField(default=True, help_text='Recommended. Displays in a section about the LIVE team.', verbose_name='viewable to partners')),
                ('full_name', models.CharField(max_length=150, verbose_name='full name')),
                ('profile_picture', models.ImageField(help_text='Please upload a 50x50 square ratio image.', upload_to='', verbose_name='profile picture')),
                ('description', models.TextField(help_text='i.e. Responsible for overseeing all logistical operations on the day of.', verbose_name='description')),
                ('email_address', models.EmailField(max_length=254, verbose_name='email address')),
                ('linkedin', models.URLField(help_text='i.e. https://www.linkedin.com/in/alvintangz/', verbose_name='linkedin account')),
                ('resume', models.FileField(upload_to='', verbose_name='resume')),
            ],
        ),
    ]
