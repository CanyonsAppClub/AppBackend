from django.db import models
from django.contrib.auth.models import User


class AppUser(models.Model):
    user = models.ForeignKey(User)
    email = models.EmailField(blank=True, null=True)
