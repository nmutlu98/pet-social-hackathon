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
from .models import Hotel
from .models import Walker
from .models import Comments

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password')


class VetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vet
        fields = ('id', 'name', 'address', 'phone')

class PetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pet
        fields = ('id', 'name', 'age', 'type', 'breed', 'gender', 'insurance', 'chronicalIllnesses', 'vaccineStatus')

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
    pet_id = serializers.CharField(source='pet.id')
    file = serializers.CharField(source='pdf')
    class Meta:
        model = Claim
        fields = ('id', 'pet_name', 'description', 'status', 'file', 'pdf', 'pet_id')

class CaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Case
        fields = ('id', 'title')

class WalkerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Walker
        fields = ('id', 'first_name', 'last_name', 'rate', 'big_image', 'background', 'date')


class HotelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hotel
        fields = ('id', 'first_name', 'last_name', 'rate', 'big_image', 'background', 'date')


class AskidaSigortaSerializer(serializers.HyperlinkedModelSerializer):
    case_name = serializers.CharField(source='case.title')
    vet_name = serializers.CharField(source='case.vet.name')
    files = serializers.CharField(source='case.bill')
    class Meta:
        model = AskidaSigorta
        fields = ('id','amount', 'isUsed', 'case_name', 'vet_name', 'files')

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comments
        fields = ('vet', 'user', 'comment', 'star', 'date')