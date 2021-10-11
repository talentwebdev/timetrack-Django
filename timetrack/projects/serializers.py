from .models import (
    Project,
    Tag,
    Task,
    TimeLogEntry
)
from rest_framework import serializers

from django.contrib.auth import get_user_model

User = get_user_model()

# models


class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Project
        fields = '__all__'
        read_only_fields = ['users']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    assignee = serializers.SlugRelatedField(
        many=True, slug_field='username', queryset=User.objects.all(), required=False)

    class Meta:
        model = Task
        fields = '__all__'


class TimeLogSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = TimeLogEntry
        fields = '__all__'

    def get_fields(self, *args, **kwargs):
        fields = super(TimeLogSerializer, self).get_fields(*args, **kwargs)
        request = self.context.get('request', None)
        if request and getattr(request, 'method', None) != "POST":
            fields['task'].read_only = True
        return fields

    def validate_task(self, value):
        """
        Check that the time log is for time log
        """

        return value
