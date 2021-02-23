# Generated by Django 2.0.3 on 2018-07-26 21:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_plugindatum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plugindatum',
            name='user',
            field=models.ForeignKey(default=None, help_text='The user this setting belongs to. If NULL, the setting is global.', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]