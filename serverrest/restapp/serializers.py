from rest_framework import serializers
from serverrest.restapp.models import PickupLine, PickupLineRating
from serverrest.restapp.choices import *

class PickupLineRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PickupLineRating
        fields = ('id', 'pickup_line', 'creation_date', 'vote', 'device_id')

class PickupLineRatingSerializerNoId(serializers.ModelSerializer):
    class Meta:
        model = PickupLineRating
        fields = ('pickup_line', 'creation_date', 'vote', 'device_id')
   
class PickupLineWithVotesCountedSerializer(serializers.ModelSerializer):
    up_votes=serializers.SerializerMethodField('count_up_votes')
    down_votes=serializers.SerializerMethodField('count_down_votes')
    class Meta:
        model = PickupLine
        fields = ('id', 'pickup_text', 'creation_date','up_votes', 'down_votes')
    def count_up_votes(self, pickup_line):
        return pickup_line.ratings.filter(vote=up_vote).count()
    def count_down_votes(self, pickup_line):
        return pickup_line.ratings.filter(vote=down_vote).count()

class PickupLineSerializer(serializers.ModelSerializer):
    ratings = PickupLineRatingSerializer(many=True)
    class Meta:
        model = PickupLine
        fields = ('id', 'pickup_text', 'creation_date','ratings',)
    
    
class PickupLineWithDeviceIDVoteSerializer(serializers.ModelSerializer):  
    device_vote=serializers.SerializerMethodField('vote_of_device')
    up_votes=serializers.SerializerMethodField('count_up_votes')
    down_votes=serializers.SerializerMethodField('count_down_votes')
    class Meta:
        model = PickupLine
        fields = ('id', 'pickup_text', 'creation_date','up_votes', 'down_votes','device_vote')
    def count_up_votes(self, pickup_line):
        return pickup_line.ratings.filter(vote=up_vote).count()
    def count_down_votes(self, pickup_line):
        return pickup_line.ratings.filter(vote=down_vote).count()
    def vote_of_device(self, pickup_line):
        try:
            return PickupLineRatingSerializer(PickupLineRating.objects.get(pickup_line=pickup_line, device_id=str(self.context['device_id']))).data 
        except PickupLineRating.DoesNotExist:
            return None
        
    
    
  