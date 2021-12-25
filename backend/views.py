from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
# Create your views here.
# views.py
from rest_framework import viewsets

from .serializers import UserSerializer
from .serializers import VetSerializer
from .serializers import ClaimSerializer
from .serializers import PetSerializer
from .serializers import CaseSerializer
from .serializers import AskidaSigortaSerializer
from .models import User
from .models import Vet
from .models import Claim
from .models import Pet
from .models import Case
from .models import AskidaSigorta

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

class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all().order_by('name')
    serializer_class = PetSerializer

    @action(detail=False, methods=["get"])
    def get_pet_by_id(self, request):
        id = request.GET.get("id")
        claims = self.get_queryset().filter(id = id)
        serializer = self.get_serializer(claims, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=["get"])
    def get_pets_of_user(self, request):
        id = request.GET.get("id")
        claims = self.get_queryset().filter(owner = id)
        serializer = self.get_serializer(claims, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ClaimViewSet(viewsets.ModelViewSet):
    queryset = Claim.objects.all().order_by('name')
    serializer_class = ClaimSerializer

    @action(detail=False, methods=["get"])
    def get_claim_by_id(self, request):
        id = request.GET.get("id")
        claims = self.get_queryset().filter(id = id)
        serializer = self.get_serializer(claims, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=["get"])
    def get_claims_of_user(self, request):
        id = request.GET.get("id")
        claims = self.get_queryset().filter(owner = id)
        serializer = self.get_serializer(claims, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CaseViewSet(viewsets.ModelViewSet):
    queryset = Case.objects.all().order_by('title')
    serializer_class = CaseSerializer

    @action(detail=False, methods=["get"])
    def get_case_by_id(self, request):
        id = request.GET.get("id")
        cases = self.get_queryset().filter(id = id)
        serializer = self.get_serializer(cases, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=["get"])
    def get_cases_of_user(self, request):
        id = request.GET.get("id")
        cases = self.get_queryset().filter(owner = id)
        serializer = self.get_serializer(cases, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AskidaSigortaViewSet(viewsets.ModelViewSet):
    queryset = AskidaSigorta.objects.all()
    serializer_class = AskidaSigortaSerializer

    @action(detail=False, methods=["get"])
    def get_case_by_id(self, request):
        id = request.GET.get("id")
        insurances = self.get_queryset().filter(id = id)
        serializer = self.get_serializer(insurances, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=["get"])
    def get_askida_sigorta_of_user(self, request):
        id = request.GET.get("id")
        insurances = self.get_queryset().filter(owner = id)
        serializer = self.get_serializer(insurances, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)