# Generated by Django 2.2.4 on 2019-08-08 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mento',
            old_name='address',
            new_name='contact',
        ),
    ]
