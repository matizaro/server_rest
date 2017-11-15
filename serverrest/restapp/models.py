from django.db import models
from serverrest.restapp.choices import *
from datetime import datetime  

class PickupLine(models.Model):
    pickup_text = models.CharField(max_length=1000)
    creation_date = models.DateTimeField('date created',default=datetime.now, blank=True)
    
    def __str__(self):
        return self.pickup_text
    
class PickupLineRating(models.Model):
    pickup_line=models.ForeignKey(PickupLine, related_name='ratings', on_delete=models.CASCADE)
    creation_date = models.DateTimeField('date created',default=datetime.now, blank=True)
    device_id=models.CharField(max_length=200, default=0)
    vote = models.IntegerField(choices=PickupLineVotes)
    
    class Meta:
        unique_together = (("pickup_line", "device_id"),)  
        
    def __str__(self):
        return self.pickup_line.pickup_text + str(self.vote)
    
    