# Generated by Django 3.0 on 2021-05-13 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CrimeReportingSystem', '0002_complaintbox_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='des',
            new_name='Description',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='mail',
            new_name='email',
        ),
    ]
