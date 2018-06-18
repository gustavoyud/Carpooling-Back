import uuid
from django.db import models
from cars.models import Cars
from destiny.models import Destiny
from car.models import Users

# Create your models here.
class Schedule(models.Model):
    schedule_pk         = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    dateTime            = models.DateTimeField()
    cars                = models.ForeignKey(Cars, on_delete=models.CASCADE)
    final_destiny       = models.ForeignKey(Destiny, on_delete=models.CASCADE)
    property_user       = models.ForeignKey(Users, related_name='user_get', on_delete=models.CASCADE)

    class Meta:
        verbose_name = u'scheduled'
        verbose_name_plural = u'scheduleds'
    
    def __str__(self):
        return str(self.final_destiny)