from django.db import models

# Create your models here.
class IndiaJobs(models.Model):
    Name = models.CharField(max_length=30)
    Education = models.CharField(max_length=30)
    City = models.CharField(max_length=30)
    Position = models.CharField(max_length=30)
