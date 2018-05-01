from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import F

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

  def perform_create(self, serializer):
    Beer.objects.filter(ranking__gte=self.request.data['ranking']).update(ranking=F('ranking') + 1)
    serializer.save()

class BeerPUT(generics.RetrieveUpdateAPIView):
  permission_classes = (IsAuthenticated, )
  queryset = Beer.objects.all()
  serializer_class = BeerSerializer

  def perform_update(self, serializer):
    old_ranking = int(Beer.objects.get(id=serializer.instance.id).ranking)
    new_ranking = int(self.request.data['ranking'])
    # Beer is movin on up in the world
    if (old_ranking > new_ranking):
      Beer.objects.filter(ranking__range=(new_ranking, old_ranking - 1)).update(ranking=F('ranking') + 1)
    # Beer is being ranked shittier
    elif (old_ranking < new_ranking):
      Beer.objects.filter(ranking__range=(old_ranking + 1, new_ranking)).update(ranking=F('ranking') - 1)
    serializer.save()

class BeerDELETE(generics.DestroyAPIView):
  permission_classes = (IsAuthenticated, )
  queryset = Beer.objects.all()
  serializer_class = BeerSerializer
