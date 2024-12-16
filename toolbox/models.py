from django.db import models

class Numbers(models.Model):
    number = models.IntegerField()
    request_ct = models.IntegerField()