from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
# Create your views here.
# views.py
from rest_framework import viewsets

from .serializers import UserSerializer
from .serializers import VetSerializer
from .models import User
from .models import Vet

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('email')
    serializer_class = UserSerializer

    @action(detail=False, methods=["get"])
    def get_user_by_credentials(self, request):
        print(request.GET)
        username = request.GET.get('user', '')
        password = request.GET.get('password', '')
        users = self.get_queryset().filter(email = username, password = password)
        serializer = self.get_serializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class VetViewSet(viewsets.ModelViewSet):
    queryset = Vet.objects.all().order_by('email')
    serializer_class = VetSerializer

    @action(detail=False, methods=["get"])
    def get_user_by_credentials(self, request):
        print(request.GET)
        username = request.GET.get('user', '')
        password = request.GET.get('password', '')
        users = self.get_queryset().filter(email = username, password = password)
        serializer = self.get_serializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)