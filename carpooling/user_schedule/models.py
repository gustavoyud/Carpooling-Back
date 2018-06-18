import uuid
from django.db import models
from schedule.models import Schedule
from car.models import User

# Create your models here.
class userSchedule(models.Model):
    user_schedule_pk    = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    schedule_id         = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    user_id             = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user_schedule_pk)