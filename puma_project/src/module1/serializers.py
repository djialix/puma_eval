from rest_framework import serializers,fields
from .models import UsersPuma
from django.db.models import Q

class Users_Serializer(serializers.ModelSerializer):

    class Meta:
        model = UsersPuma
        fields = '__all__'

