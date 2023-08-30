from rest_framework import viewsets, filters
from .models import UsersPuma
from .serializers import Users_Serializer


class User_ViewSet(viewsets.ModelViewSet):
    queryset = UsersPuma.objects.all()
    #style = {'base_template': 'imput.htlm'}
    serializer_class = Users_Serializer


