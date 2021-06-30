from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=100)
    contact=models.CharField(max_length=30)
    interests=models.CharField(max_length=300)
