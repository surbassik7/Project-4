from django.conf import settings
from django.contrib.gis.geos import Point
from django.http import JsonResponse
from rest_framework import permissions, viewsets
from rest_framework.views import APIView

from spot_me import models as spot_me_models
from spot_me import serializers as spot_me_serializers


class SearchViewSet(viewsets.ModelViewSet):
    serializer_class = spot_me_serializers.SearchSerializer
    queryset = spot_me_models.Search.objects.all()



