# Generated by Django 4.1.3 on 2022-12-12 06:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Europa', '0005_comment_countcomments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='countcomments',
        ),
    ]
