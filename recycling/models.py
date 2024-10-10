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
    total_fund = models.IntegerField(default=0.0)
    withdrawn_fund = models.IntegerField(default=0.0)
    location = models.CharField(null=True, blank=True, max_length=300)
    Phone = models.CharField(max_length=15, null=True, blank=False)
    pickup = models.BooleanField(default=False)
    DropOff = models.BooleanField(default=False)



class FundRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    CHOICES = [
        ("Health", "Health Care Need"),
        ("School", "Educational Need"),
        ("EcoFashion", "Eco Fashion"),
        ("EcoFashion", "Eco Fashion"),
        ("MTN Airtime", "MTN Airtime"),
        ("GLO Airtime", "GLO Airtime"),
        ("AirTel Airtime", "AirTel Airtime"),
        ("9Mobile Airtime", "9Mobile Airtime"),
        ("MTN Data", "MTN Data"),
        ("GLO Data", "GLO Data"),
        ("AirTel Data", "AirTel Data"),
        ("9Mobile Data", "9Mobile Data"),
    ]
    withdraw_type = models.CharField(choices=CHOICES,  max_length=100, default="")
    request_date = models.DateTimeField(auto_now_add=True)
    disbursed = models.BooleanField(default=False)
    amount = models.IntegerField(null=True, blank=True)
    account_no = models.CharField(null=False, blank=False, max_length=1000)

