from django.db import models
from multiselectfield import MultiSelectField
from users.models import CustomUser


class TrashRequest(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    TRASH_CHOICES = [
        ('Nylon', 'Nylon'),
        ('Bottle', 'Bottle'),
        ('Plastic', 'Plastic'),
    ]
    trash_types = MultiSelectField(choices=TRASH_CHOICES, max_choices=3, max_length=100, default="")
    pickup = models.BooleanField(default=False)
    DropOff = models.BooleanField(default=False)
    request_date = models.DateTimeField(auto_now_add=True)
    seen = models.BooleanField(default=False)
    finished = models.BooleanField(default=False)
    weight = models.IntegerField(null=True, blank=True)
    earned = models.IntegerField(null=True, blank=True)
    trash_type = models.CharField(null=False, blank=True, default="", max_length=20)
    location = models.CharField(null=True, blank=True, max_length=300)
    Phone = models.CharField(max_length=15, null=True, blank=False)


class FundRequest(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    CHOICES1 = [
        ("Withdraw purpose", "Withdraw purpose"),
        ("Health", "Health Care Need"),
        ("School", "Educational Need"),
        ("EcoFashion", "Eco Fashion"),
        ("Airtime", "Airtime"),
        ("Data", "Data"),
        ("others", "Others"),

        
    ]
    Health = [
        ("Choose purpose", "Choose purpose"),
        ("Medication", "Medication"),
        ("Medical test", "Medical test"),
        ("Hospital bill", "Hospital bill"),
        ("others", "Others"),
    ]
    School = [
        ("School Purpose", "School Purpose"),
        ("School fee", "School fee"),
        ("feeding", "feeding"),
        ("Book / Course materials", "Book / Course materials"),
        ("others", "Others"),
    ]
    Airtime = [
        ("Airtime Network", "Airtime Network"),
        ("MTN Airtime", "MTN Airtime"),
        ("GLO Airtime", "GLO Airtime"),
        ("AirTel Airtime", "AirTel Airtime"),
        ("9Mobile Airtime", "9Mobile Airtime"),
    ]
    Data = [
        ("Data Network", "Data Network"),
        ("MTN Data", "MTN Data"),
        ("GLO Data", "GLO Data"),
        ("AirTel Data", "AirTel Data"),
        ("9Mobile Data", "9Mobile Data"),
    ]
    withdraw_type = models.CharField(choices=CHOICES1,  max_length=100, default="Withdraw purpose")
    data_choice = models.CharField(choices=Data, max_length=100, default="Data Network", null=True, blank=True)
    airtime_choice = models.CharField(choices=Airtime, max_length=100, default="Airtime Network", null=True, blank=True)
    school_choice = models.CharField(choices=School, max_length=100, default="School Purpose", null=True, blank=True)
    health_choice = models.CharField(choices=Health, max_length=100, default="Choose purpose", null=True, blank=True)
    request_date = models.DateTimeField(auto_now_add=True)
    disbursed = models.BooleanField(default=False)
    amount = models.IntegerField(null=False, blank=False)
    account_no = models.CharField(null=True, blank=True, max_length=1000)
    others = models.CharField(null=True, blank=True, max_length=10000)
    bank = models.CharField(null=True, blank=True, max_length=1000)
    Phone = models.CharField(max_length=15, null=True, blank=True)
    account_name = models.CharField(null=True, blank=True, max_length=1000)
    seen = models.BooleanField(default=False)
    finished = models.BooleanField(default=False)


