# Generated by Django 2.1.2 on 2018-12-18 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageWidget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(help_text="Display an image in the widget.<br/><strong>Recommended that you have an image with large dimensions so it can be stretched based off user's screen.</strong>", upload_to='notifications/widget/', verbose_name='image')),
            ],
            options={
                'verbose_name': 'portal image widget',
            },
        ),
        migrations.CreateModel(
            name='PortalWidget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('show_title', models.BooleanField(default=True, help_text='Let the widget title be seen publicly.')),
                ('show_delegate', models.BooleanField(default=False)),
                ('show_partner', models.BooleanField(default=False)),
                ('pinned', models.BooleanField(default=False, help_text='Pin this at the top of the portal.')),
                ('external_link', models.URLField(blank=True, help_text='Add a link to an external source. Entire widget will be clickable.', verbose_name='external link')),
            ],
            options={
                'verbose_name': 'portal widget',
            },
        ),
        migrations.CreateModel(
            name='TextNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Text at 2018-12-18 12:27:09.766464', max_length=100, verbose_name='title')),
                ('message', models.TextField(help_text='Display a piece of text in the widget.', verbose_name='message')),
                ('send', models.BooleanField(default=False, help_text='If True, message will be sent after submitting this form.', verbose_name='send now')),
                ('sent', models.BooleanField(default=False, help_text='If True, message has been sent to all delegates.', verbose_name='sent')),
                ('sent_time', models.DateTimeField(blank=True, null=True, verbose_name='time message sent')),
            ],
        ),
        migrations.CreateModel(
            name='TextWidget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(help_text='Display a piece of text in the widget.', verbose_name='text')),
                ('widget', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='text_widget', to='notifications.PortalWidget')),
            ],
            options={
                'verbose_name': 'portal text widget',
            },
        ),
        migrations.AddField(
            model_name='imagewidget',
            name='widget',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='image_widget', to='notifications.PortalWidget'),
        ),
        migrations.CreateModel(
            name='ImageWidgetProxy',
            fields=[
            ],
            options={
                'verbose_name': 'image widget',
                'proxy': True,
                'indexes': [],
            },
            bases=('notifications.portalwidget',),
        ),
        migrations.CreateModel(
            name='TextWidgetProxy',
            fields=[
            ],
            options={
                'verbose_name': 'text widget',
                'proxy': True,
                'indexes': [],
            },
            bases=('notifications.portalwidget',),
        ),
    ]
