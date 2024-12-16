from django.db import models

class Numbers(models.Model):
    """
        Rudimentary model to store numbers and request count and recent calls
    """
    number = models.IntegerField()
    request_ct = models.IntegerField()
    request_last_timestamp = models.DateTimeField(null=True, blank=True)

    # added to fix the admin view
    class Meta:
        verbose_name = "Number"

    def __str__(self):
        return f"{self.number}"