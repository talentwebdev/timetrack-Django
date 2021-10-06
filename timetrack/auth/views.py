from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer

from django.contrib.auth import get_user_model

from .serializers import UserSerializer


@api_view(['POST', ])
def registration_view(request):

    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data = UserSerializer(account).data
            data['token'] = Token.objects.create(user=account).key
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

     # create customer with account info
    return Response(data)


class UserLoginView(APIView):
    serializer_class = AuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        user_serializer = UserSerializer(user)
        token, _ = Token.objects.get_or_create(user=user)
        data = user_serializer.data
        data['token'] = token.key
        return Response(data)
