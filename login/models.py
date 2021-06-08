from django.db import models

class reg(models.Model):
    username=models.CharField(max_length=200)
    email=models.EmailField()
    password=models.CharField(max_length=50)
    number=models.BigIntegerField()
