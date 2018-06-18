from django.db import models

# Create your models here.
class Destiny(models.Model):
    destiny_pk          = models.AutoField(primary_key=True)
    address             = models.CharField(max_length=30)
    complement          = models.CharField(max_length=30)
    zip                 = models.IntegerField()
    neighborhood        = models.CharField(max_length=30)
    city                = models.CharField(max_length=30)
    federal_unit        = models.CharField(max_length=2)
    phone               = models.IntegerField()

    class Meta:
        verbose_name = u'destiny'
        verbose_name_plural = u'destinys'
    
    def __str__(self):
        return str(self.destiny_pk)