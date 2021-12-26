from django.contrib import admin
from .models import Comments, User
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

# Register your models here.
admin.site.register(User)
admin.site.register(Pet)
admin.site.register(Vet)
admin.site.register(Vaccination)
admin.site.register(VaccinationCard)
admin.site.register(Company)
admin.site.register(Claim)
admin.site.register(AskidaSigorta)
admin.site.register(Case)
admin.site.register(Hotel)
admin.site.register(Walker)
admin.site.register(Comments)