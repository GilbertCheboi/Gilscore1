# Generated by Django 4.1.3 on 2022-11-30 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='Afcon',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='Baseball',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='Bundesliga',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='Europa',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='Formula1',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='Laliga',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='NBA',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='NFL',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='Worldcup',
        ),
    ]
