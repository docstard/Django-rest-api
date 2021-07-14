from rest_framework import fields, serializers
from .models import User_api

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_api
        fields = '__all__'