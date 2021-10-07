from .models import (
    Task
)
import django_filters as filters


class TaskFilter(filters.FilterSet):
    class Meta:
        model = Task
        fields = {
            'name': ['icontains', 'exact']
        }
