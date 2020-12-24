from django.db import models

# Create your models here.

class Personal_info(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    married = models.BooleanField()
    city = models.CharField(max_length=30)


class Academic_info(models.Model):
    course = models.CharField(max_length=30)
    passing_year = models.IntegerField


class Experience_info(models.Model):
    company_name = models.CharField(max_length=30)
    job_role = models.CharField(max_length=30)
    Years = models.IntegerField

