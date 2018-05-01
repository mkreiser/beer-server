from django.contrib.admin.views.decorators import staff_member_required

from rest_framework import filters, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from beerApp.models import Beer
from beerApp.serializers import BeerSerializer

# Root page directory
@api_view(('GET',))
@permission_classes((AllowAny,))
def api_root(request, format=None):
    return Response({ "routes": [
      "GET ALL Beers: https://kreiserbeerserver.herokuapp.com/beers/",
      "GET Beer: https://kreiserbeerserver.herokuapp.com/beers/pourBeer/[id]/",
      "POST Beer: https://kreiserbeerserver.herokuapp.com/beers/brewBeer/",
      "PUT Beer: https://kreiserbeerserver.herokuapp.com/beers/mixBeer/[id]/",
      "DELETE Beer: https://kreiserbeerserver.herokuapp.com/beers/tossBeer/[id]/",
    ]})

# MEET SERIALIZERS
class BeerGETAll(generics.ListAPIView):
  permission_classes = (AllowAny, )
  queryset = Beer.objects.all()
  serializer_class = BeerSerializer
  filter_backends = (filters.SearchFilter,)
  search_fields = ['name']

class BeerGET(generics.RetrieveAPIView):
  permission_classes = (AllowAny, )
  queryset = Beer.objects.all()
  serializer_class = BeerSerializer

class BeerPOST(generics.CreateAPIView):
  permission_classes = (IsAuthenticated, )
  queryset = Beer.objects.all()
  serializer_class = BeerSerializer

class BeerPUT(generics.RetrieveUpdateAPIView):
  permission_classes = (IsAuthenticated, )
  queryset = Beer.objects.all()
  serializer_class = BeerSerializer

class BeerDELETE(generics.DestroyAPIView):
  permission_classes = (IsAuthenticated, )
  queryset = Beer.objects.all()
  serializer_class = BeerSerializer
