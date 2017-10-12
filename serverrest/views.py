from rest_framework import viewsets
from serverrest.restapp.serializers import PickupLineSerializer, PickupLineRatingSerializer
from serverrest.restapp.models import PickupLine, PickupLineRating

class PickupLineViewSet(viewsets.ModelViewSet):
    queryset = PickupLine.objects.all().order_by('-creation_date')
    serializer_class = PickupLineSerializer


class PickupLineRatingViewSet(viewsets.ModelViewSet):
    queryset = PickupLineRating.objects.all()
    serializer_class = PickupLineRatingSerializer