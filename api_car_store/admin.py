from django.contrib import admin

# Register your models here.
from .models import Dealer, Car

admin.site.register(Dealer)
admin.site.register(Car)
