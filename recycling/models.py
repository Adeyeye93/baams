from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField

class TrashRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    TRASH_CHOICES = [
        ('Nylon', 'Nylon'),
        ('Bottle', 'Bottle'),
        ('Plastic', 'Plastic'),
    ]
    trash_types = MultiSelectField(choices=TRASH_CHOICES, max_choices=3, max_length=100, default="")
    request_date = models.DateTimeField(auto_now_add=True)
    seen = models.BooleanField(default=False)
    finished = models.BooleanField(default=False)
    weight = models.IntegerField(null=True, blank=True)
    points = models.IntegerField(null=True, blank=True)
    trash_type = models.CharField(null=False, blank=True, default="", max_length=20)
