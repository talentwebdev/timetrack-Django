import django_filters

from rest_framework import filters
from rest_framework import viewsets
from rest_framework.routers import DefaultRouter
from rest_framework.permissions import IsAuthenticated


from .models import (
    Project,
    Task,
    Tag
)
from .serializers import (
    ProjectSerializer,
    TagSerializer,
    TaskSerializer,
    TimeLogSerializer
)
from .permissions import (
    IsOwnerOrReadOnly,
    IsTaskOwner
)
from .filters import (
    TaskFilter,
    TimeLogFilter 
)

# Create your views here.


class ProjectViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the actions for project
    """
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly, )

    def get_queryset(self):
        return self.request.user.projects.all() | self.request.user.own_projects.all()


class TagViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the actions for tags
    """
    serializer_class = TagSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Tag.objects.all()


class TaskViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the actions for tasks
    """

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated, IsTaskOwner, )
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_class = TaskFilter


class TimeLogViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the actions for time logs
    """
    serializer_class = TimeLogSerializer
    permission_classes = (IsAuthenticated, )
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_class = TimeLogFilter

    def get_queryset(self):
        return self.request.user.time_logs.all()


router = DefaultRouter()
router.register(r'api/projects', ProjectViewSet, basename='projects')
router.register(r'api/tags', TagViewSet, basename='tags')
router.register(r'api/tasks', TaskViewSet, basename='tasks')
router.register(r'api/timelogs', TimeLogViewSet, basename='timelogs')
