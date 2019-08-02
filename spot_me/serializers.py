from rest_framework_gis import serializers

from spot_me import models as spot_me_models


class SearchSerializer(serializers.GeoModelSerializer):

    class Meta:
        model = spot_me_models.Search
        exclude = []