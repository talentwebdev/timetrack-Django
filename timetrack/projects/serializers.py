from rest_framework import serializers

from django.contrib.auth import get_user_model

User = get_user_model()

# models
from .models import (
    Project,
    Tag,
    Task
)


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
    assignee = serializers.SlugRelatedField(many=True, slug_field='username', queryset=User.objects.all())

    class Meta:
        model = Task
        fields = '__all__'
