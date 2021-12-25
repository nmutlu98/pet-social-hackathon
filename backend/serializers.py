# serializers.py
from rest_framework import serializers

from .models import User
from .models import Vet
from .models import Pet
from .models import Vaccination
from .models import VaccinationCard
from .models import Company
from .models import Claim
from .models import Case
from .models import AskidaSigorta

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
        fields = ('id', 'name', 'age', 'type', 'breed', 'gender', 'insurance', 'vaccineStatus')

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
    pet_name = serializers.CharField(source='pet.name')
    class Meta:
        model = Claim
        fields = ('id', 'pet_name', 'description', 'pet', 'status')

class CaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Case
        fields = ('id', 'title')

class AskidaSigortaSerializer(serializers.HyperlinkedModelSerializer):
    owner_name = serializers.CharField(source='owner.name')
    vet_name = serializers.CharField(source='vet.name')
    case_name = serializers.CharField(source='case.title')
    class Meta:
        model = AskidaSigorta
        fields = ('id', 'case', 'case_name', 'vet_name', 'amount')