# serializers.py
from rest_framework import serializers

from .models import User
from .models import Vet
from .models import Pet
from .models import Vaccination
from .models import VaccinationCard
from .models import Company
from .models import Claim

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password')


class VetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vet
        fields = ('id', 'name')

class PetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pet
        fields = ('id', 'name')

class VaccinationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vaccination
        fields = ('id', 'name')

class VaccinationCardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VaccinationCard
        fields = ('id')

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name')

class ClaimSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Claim
        fields = ('id', 'name', 'description')