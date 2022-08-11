from email import message
from django.db import models

# Create your models here.

class FeedBack(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.IntegerField(null=True, blank=True)
    feed = models.TextField(null = True, blank=True)

    def __str__(self) -> str:
        return self.name
