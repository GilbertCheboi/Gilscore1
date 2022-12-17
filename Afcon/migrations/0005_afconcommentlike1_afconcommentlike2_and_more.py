# Generated by Django 4.1.3 on 2022-12-16 04:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Afcon', '0004_afconvideo_commentafconvideo'),
    ]

    operations = [
        migrations.CreateModel(
            name='AfconCommentLike1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='AfconCommentLike2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='AfconCommentLike3',
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
                ('comment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Afcon_comments1', to='Afcon.comment')),
                ('likes', models.ManyToManyField(blank=True, related_name='Afconcomment_user1', through='Afcon.AfconCommentLike1', to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Afcon.comment1')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Afconcomments1', to=settings.AUTH_USER_MODEL)),
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
                ('comment1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Afcon_comments2', to='Afcon.comment1')),
                ('likes', models.ManyToManyField(blank=True, related_name='Afconcomment_user2', through='Afcon.AfconCommentLike2', to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Afcon.comment2')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Afconcomments2', to=settings.AUTH_USER_MODEL)),
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
                ('comment2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Afcon_comments3', to='Afcon.comment2')),
                ('likes', models.ManyToManyField(blank=True, related_name='Afconcomment_user3', through='Afcon.AfconCommentLike3', to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Afcon.comment3')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Afconcomments3', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.AddField(
            model_name='afconcommentlike3',
            name='comment3',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Afcon.comment3'),
        ),
        migrations.AddField(
            model_name='afconcommentlike3',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='afconcommentlike2',
            name='comment2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Afcon.comment2'),
        ),
        migrations.AddField(
            model_name='afconcommentlike2',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='afconcommentlike1',
            name='comment1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Afcon.comment1'),
        ),
        migrations.AddField(
            model_name='afconcommentlike1',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
