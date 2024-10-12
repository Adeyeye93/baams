from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    total_fund = models.IntegerField(default=0.0, null=True, blank=True)
    withdrawn_fund = models.IntegerField(default=0.0, null=True, blank=True)
