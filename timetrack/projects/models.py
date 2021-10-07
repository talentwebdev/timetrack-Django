from django.db import models
from core.models import TimeStampedModel
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

# Create your models here.
User = get_user_model()


class Project(TimeStampedModel):
    owner = models.ForeignKey(
        User, related_name="own_projects", on_delete=models.CASCADE, help_text=_("Owner of project"))
    name = models.CharField(max_length=255, null=True,
                            blank=True, help_text=_("Name of project"))
    description = models.TextField(
        null=True, blank=True, help_text=_("Description"))
    users = models.ManyToManyField(
        User, related_name="projects", help_text=_("Users added to this project"))


class Tag(TimeStampedModel):
    name = models.CharField(
        max_length=255, primary_key=True, help_text=_("Tag name"))


class Task(TimeStampedModel):
    PRIORITY_CHOICES = (
        ("LOW", "low"),
        ("MEDIUM", "medium"),
        ("HIGH", "high"),
    )

    project = models.ForeignKey(
        Project, related_name="tasks", on_delete=models.CASCADE, help_text=_("Project"))
    owner = models.ForeignKey(
        User, related_name="own_tasks", on_delete=models.CASCADE, help_text=_("Owner of task"))
    name = models.CharField(max_length=255, null=True,
                            blank=True, help_text=_("Task name"))
    assignee = models.ManyToManyField(
        User, related_name="tasks", help_text=_("Users assgined to this task"))
    due_date = models.DateTimeField(
        null=True, blank=True, help_text=_("Due date"))
    priority = models.CharField(
        max_length=10, choices=PRIORITY_CHOICES, default=None, help_text=_("Priority choices"))
    estimated_time = models.TimeField(
        null=True, blank=True, help_text=_("Estimated time for task"))
    start_date = models.DateField(
        null=True, blank=True, help_text=_("Task started date"))
    tags = models.ManyToManyField(
        Tag, related_name="tasks", help_text=_("Tags attached to the task"))


class TimeLogEntry(TimeStampedModel):
    task = models.ForeignKey(
        Task, related_name="time_logs", on_delete=models.CASCADE, help_text=_("Task which time log entry included into"))
    user = models.ForeignKey(
        User, related_name="time_logs", on_delete=models.CASCADE, help_text=_("User"))
    description = models.TextField(
        null=True, blank=True, help_text=_("Description of time log entry"))
    completed = models.BooleanField(default=False, help_text=_("Completed"))
    paused = models.BooleanField(default=False)
    log_start_time = models.DateTimeField(
        null=True, blank=True, help_text=_("Log started time"))
    ttl_logged_time = models.TimeField()
