# myapi/urls.py
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'vets', views.VetViewSet)
router.register(r'claims', views.ClaimViewSet)
router.register(r'pets', views.PetViewSet)
router.register(r'cases', views.CaseViewSet)
router.register(r'askidaSigorta', views.AskidaSigortaViewSet)
router.register(r'hotels', views.HotelViewSet)
router.register(r'walkers', views.WalkerViewSet)
router.register(r'comments', views.CommentsViewSet)
# path('path/to/my/view/', MySimpleView.as_view())

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]