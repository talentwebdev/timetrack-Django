# Generated by Django 3.2.8 on 2021-10-07 08:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, help_text='Name of project', max_length=255, null=True)),
                ('description', models.TextField(blank=True, help_text='Description', null=True)),
                ('owner', models.ForeignKey(help_text='Owner of project', on_delete=django.db.models.deletion.CASCADE, related_name='own_projects', to=settings.AUTH_USER_MODEL)),
                ('users', models.ManyToManyField(help_text='Users added to this project', related_name='projects', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text='Tag name', max_length=255, primary_key=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, help_text='Task name', max_length=255, null=True)),
                ('due_date', models.DateTimeField(blank=True, help_text='Due date', null=True)),
                ('priority', models.CharField(choices=[('LOW', 'low'), ('MEDIUM', 'medium'), ('HIGH', 'high')], default=None, help_text='Priority choices', max_length=10)),
                ('estimated_time', models.TimeField(blank=True, help_text='Estimated time for task', null=True)),
                ('start_date', models.DateField(blank=True, help_text='Task started date', null=True)),
                ('assignee', models.ManyToManyField(help_text='Users assgined to this task', related_name='tasks', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(help_text='Owner of task', on_delete=django.db.models.deletion.CASCADE, related_name='own_tasks', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(help_text='Project', on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='projects.project')),
                ('tags', models.ManyToManyField(help_text='Tags attached to the task', related_name='tasks', to='projects.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TimeLogEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(blank=True, help_text='Description of time log entry', null=True)),
                ('completed', models.BooleanField(default=False, help_text='Completed')),
                ('paused', models.BooleanField(default=False)),
                ('log_start_time', models.DateTimeField(blank=True, help_text='Log started time', null=True)),
                ('ttl_logged_time', models.TimeField()),
                ('task', models.ForeignKey(help_text='Task which time log entry included into', on_delete=django.db.models.deletion.CASCADE, related_name='time_logs', to='projects.task')),
                ('user', models.ForeignKey(help_text='User', on_delete=django.db.models.deletion.CASCADE, related_name='time_logs', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
