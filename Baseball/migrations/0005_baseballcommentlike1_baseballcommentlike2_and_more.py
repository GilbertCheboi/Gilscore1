# Generated by Django 4.1.3 on 2022-12-16 07:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Baseball', '0004_baseballvideo_commentbaseballvideo'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseballCommentLike1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='BaseballCommentLike2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='BaseballCommentLike3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, null=True)),
                ('video', models.FileField(blank=True, null=True, upload_to='videos/')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('comment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Basbeball_comments1', to='Baseball.comment')),
                ('likes', models.ManyToManyField(blank=True, related_name='Baseballcomment_user1', through='Baseball.BaseballCommentLike1', to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Baseball.comment1')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Baseballcomments1', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Comment2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, null=True)),
                ('video', models.FileField(blank=True, null=True, upload_to='videos/')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('comment1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Baseball_comments2', to='Baseball.comment1')),
                ('likes', models.ManyToManyField(blank=True, related_name='Baseballcomment_user2', through='Baseball.BaseballCommentLike2', to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Baseball.comment2')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Baseballcomments2', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Comment3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, null=True)),
                ('video', models.FileField(blank=True, null=True, upload_to='videos/')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('comment2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Baseball_comments3', to='Baseball.comment2')),
                ('likes', models.ManyToManyField(blank=True, related_name='Baseballcomment_user3', through='Baseball.BaseballCommentLike3', to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Baseball.comment3')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Baseballcomments3', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.AddField(
            model_name='baseballcommentlike3',
            name='comment3',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Baseball.comment3'),
        ),
        migrations.AddField(
            model_name='baseballcommentlike3',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='baseballcommentlike2',
            name='comment2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Baseball.comment2'),
        ),
        migrations.AddField(
            model_name='baseballcommentlike2',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='baseballcommentlike1',
            name='comment1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Baseball.comment1'),
        ),
        migrations.AddField(
            model_name='baseballcommentlike1',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
