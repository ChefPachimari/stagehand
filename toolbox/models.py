from django.db import models

class Numbers(models.Model):
    number = models.IntegerField()
    request_ct = models.IntegerField()
    request_last_timestamp = models.DateTimeField(null=True, blank=True)