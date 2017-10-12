from rest_framework import serializers
from serverrest.restapp.models import PickupLine, PickupLineRating



class PickupLineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PickupLine
        fields = ('pickup_text', 'creation_date')


class PickupLineRatingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PickupLineRating
        fields = ('pickup_line', 'creation_date', 'vote')