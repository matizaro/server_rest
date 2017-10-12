from django.db import models
from datetime import datetime  

class PickupLine(models.Model):
    pickup_text = models.CharField(max_length=1000)
    creation_date = models.DateTimeField('date created',default=datetime.now, blank=True)
    
    def __str__(self):
        return self.pickup_text
    
class PickupLineRating(models.Model):
    pickup_line=models.ForeignKey(PickupLine, on_delete=models.CASCADE)
    creation_date = models.DateTimeField('date created',default=datetime.now, blank=True)
    vote = models.BooleanField()
    
    def __str__(self):
        return self.pickup_line.pickup_text