from rest_framework import serializers
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = UserModel
        fields = ("id", "email", "first_name",
                  "last_name", "username", "password", )

        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = UserModel.objects.create_user(
            **self.validated_data
        )

        return user
