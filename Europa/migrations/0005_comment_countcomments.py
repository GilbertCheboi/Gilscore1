# Generated by Django 4.1.3 on 2022-12-12 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Europa', '0004_commenteuropavideo_europavideo'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='countcomments',
            field=models.ForeignKey(blank='True', null='True', on_delete=django.db.models.deletion.CASCADE, related_name='count_comments', to='Europa.comment'),
            preserve_default='True',
        ),
    ]
