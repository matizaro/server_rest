from rest_framework import viewsets, mixins
from serverrest.restapp.serializers import PickupLineSerializer, PickupLineRatingSerializer, PickupLineWithVotesCountedSerializer, PickupLineWithDeviceIDVoteSerializer, PickupLineRatingSerializerNoId
from serverrest.restapp.models import PickupLine, PickupLineRating
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from datetime import datetime  

class PickupLineViewSet(mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                              viewsets.GenericViewSet):
    queryset = PickupLine.objects.all().order_by('-creation_date')
    serializer_class = PickupLineSerializer

class PickupLineRatingViewSet(mixins.CreateModelMixin,
                                mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                mixins.UpdateModelMixin,
                              viewsets.GenericViewSet):
    queryset = PickupLineRating.objects.all()
    serializer_class = PickupLineRatingSerializer
    
    def create(self, request):
        try:
            oldRating=PickupLineRating.objects.get(pickup_line=request.data['pickup_line'], device_id=request.data['device_id'])
            oldRating.delete()
        except:
            pass
              
        rating = PickupLineRatingSerializerNoId(data=request.data)
        rating.creation_date=datetime.now()
        if rating.is_valid():
            rating.save()
            return Response(rating.data, status=status.HTTP_201_CREATED)
        else:
            return Response(rating.errors, status=status.HTTP_400_BAD_REQUEST)
                
            
    
class PickupLineVoteCounterViewSet(mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                              viewsets.GenericViewSet):
    queryset = PickupLine.objects.all().order_by('-creation_date')
    serializer_class = PickupLineWithVotesCountedSerializer
    
class DeviceIDVotes(mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                              viewsets.GenericViewSet):
    queryset = PickupLineRating.objects.all()
    serializer_class = PickupLineRatingSerializer   


class PickupLineDeviceIDViewSet(mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                              viewsets.GenericViewSet):
    queryset = PickupLine.objects.all()
    serializer_class = PickupLineWithDeviceIDVoteSerializer
    def get_serializer_context(self):
        return {'device_id': self.kwargs.get('device_id')}
        