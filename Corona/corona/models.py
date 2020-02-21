from django.db import models

# Create your models here.
class Corona(models.Model):
    date = models.CharField(max_length=100)
    search_name = models.CharField(max_length= 200)

    def __str__(self):
        return self.search_name + " : " + self.date

class Mask(models.Model):
    date = models.CharField(max_length=100)
    search_name = models.CharField(max_length= 200)

    def __str__(self):
        return self.search_name + " : " + self.date