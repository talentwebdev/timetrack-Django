from django.urls import path
from auth.views import (
    registration_view,
    UserLoginView
)

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path(r'api/auth/register/',
         registration_view, name='register'),
    path('api/auth/login/', UserLoginView.as_view(), name='login'),
]
