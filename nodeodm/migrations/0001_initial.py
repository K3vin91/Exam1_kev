# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-06 16:32
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProcessingNode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(help_text='Hostname or IP address where the node is located (can be an internal hostname as well). If you are using Docker, this is never 127.0.0.1 or localhost. Find the IP address of your host machine by running ifconfig on Linux or by checking your network settings.', max_length=255)),
                ('port', models.PositiveIntegerField(help_text="Port that connects to the node's API")),
                ('api_version', models.CharField(help_text='API version used by the node', max_length=32, null=True)),
                ('last_refreshed', models.DateTimeField(help_text='When was the information about this node last retrieved?', null=True)),
                ('queue_count', models.PositiveIntegerField(default=0, help_text='Number of tasks currently being processed by this node (as reported by the node itself)')),
                ('available_options', django.contrib.postgres.fields.jsonb.JSONField(default={}, help_text='Description of the options that can be used for processing')),
            ],
        ),
        migrations.CreateModel(
            name='ProcessingNodeGroupObjectPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nodeodm.ProcessingNode')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
                ('permission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.Permission')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProcessingNodeUserObjectPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nodeodm.ProcessingNode')),
                ('permission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.Permission')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterUniqueTogether(
            name='processingnodeuserobjectpermission',
            unique_together=set([('user', 'permission', 'content_object')]),
        ),
        migrations.AlterUniqueTogether(
            name='processingnodegroupobjectpermission',
            unique_together=set([('group', 'permission', 'content_object')]),
        ),
    ]
