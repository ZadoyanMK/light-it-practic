from django.db import models
from django.contrib.auth.models import User
from .Links import Links


class Featured(models.Model):
    
    link = models.ForeignKey(
        to=Links, on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        to=User, on_delete=models.CASCADE
    )
