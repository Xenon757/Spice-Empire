from django.db import models
from django.contrib.auth.models import User


class business(models.Model):
    ceo = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    spiceAmount = models.BigIntegerField(null=True)

    def __str__(self):
        return self.name
