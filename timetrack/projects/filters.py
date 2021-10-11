from .models import (
    Task, TimeLogEntry
)
import django_filters as filters
from django.contrib.auth import get_user_model


class TaskFilter(filters.FilterSet):
    assignee = filters.ModelMultipleChoiceFilter(
        queryset=get_user_model().objects.all())

    class Meta:
        model = Task
        fields = {
            'owner': ['exact'],
            'name': ['icontains', 'exact'],
            'due_date': ['lt', 'gt'],
            'priority': ['exact'],
            'estimated_time': ['lt', 'gt'],
            'start_date': ['lt', 'gt'],
            'created_at': ['lt', 'gt']
        }


class TimeLogFilter(filters.FilterSet):
    created_at__lt = filters.DateTimeFilter(
        field_name='created_at', lookup_expr='lt')
    created_at__gt = filters.DateTimeFilter(
        field_name='created_at', lookup_expr='gt')

    class Meta:
        model = TimeLogEntry
        fields = {
            'task', 'user', 'description', 'completed', 'paused', 'ttl_logged_time'
        }
