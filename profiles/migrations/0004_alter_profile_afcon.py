# Generated by Django 4.1.3 on 2022-11-30 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_profile_afcon_profile_baseball_profile_bundesliga_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Afcon',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.afconleague'),
        ),
    ]