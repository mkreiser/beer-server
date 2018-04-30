from rest_framework import serializers
from beerApp.models import Beer

class BeerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Beer
    fields = ('id', 'ranking', 'brewery', 'name', 'type', 'subtype', 'city', 'state', 'country', 'comments', 'tags')
