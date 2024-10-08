from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(TrashRequest)
admin.site.register(FundRequest)
