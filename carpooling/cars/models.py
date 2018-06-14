from django.db import models
from car.models import User

# Create your models here.
class Cars(models.Model):
    car_pk          = models.AutoField(primary_key=True)
    model           = models.CharField(max_length=30)
    license_plate   = models.CharField(max_length=20)
    color           = models.CharField(max_length=20)
    capacity        = models.IntegerField()
    user            = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = u'car'
        verbose_name_plural = u'cars'
        
    def __str__(self):
        return str(self.car_pk)