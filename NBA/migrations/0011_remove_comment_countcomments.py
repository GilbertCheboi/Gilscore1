# Generated by Django 4.1.3 on 2022-12-12 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NBA', '0010_remove_tweet_comments_comment_countcomments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='countcomments',
        ),
    ]
