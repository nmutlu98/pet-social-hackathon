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
from .serializers import WalkerSerializer
from .serializers import HotelSerializer
from .serializers import CommentSerializer

from .models import User
from .models import Vet
from .models import Claim
from .models import Pet
from .models import Case
from .models import AskidaSigorta
from .models import Hotel
from .models import Walker
from .models import Comments

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
    
    def create(self, request):
        file_uploaded = request.FILES.get('file_uploaded')
        content_type = file_uploaded.content_type
        response = "POST API and you have uploaded a {} file".format(content_type)
        return Response(response)

       
    
    @action(detail=False, methods=["get"])
    def get_pets_of_user(self, request):
        id = request.GET.get("id")
        claims = self.get_queryset().filter(owner = id)
        serializer = self.get_serializer(claims, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class WalkerViewSet(viewsets.ModelViewSet):
        queryset = Walker.objects.all().order_by('first_name')
        serializer_class = WalkerSerializer

        @action(detail=False, methods=["get"])
        def get_walker_by_id(self, request):
            id = request.GET.get("id")
            walkers = self.get_queryset().filter(id = id)
            serializer = self.get_serializer(walkers, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

class HotelViewSet(viewsets.ModelViewSet):
        queryset = Hotel.objects.all().order_by('first_name')
        serializer_class = HotelSerializer

        @action(detail=False, methods=["get"])
        def get_hotel_by_id(self, request):
            id = request.GET.get("id")
            hotels = self.get_queryset().filter(id = id)
            serializer = self.get_serializer(hotels, many=True)
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

    def create(self, request):
        #file_uploaded = request.FILES.get('file_uploaded')
        #content_type = file_uploaded.content_type
        pet_id = request.POST.get("pet_id")
        statusStr = request.POST.get("status")
        description = request.POST.get("description")
        
        return Response('{"succes" : "true"}', status=status.HTTP_200_OK)
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

class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all().order_by('date')
    serializer_class = CommentSerializer

    @action(detail=False)
    def get_comments(self, request):
        comments = self.get_queryset()
        serializer = self.get_serializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)