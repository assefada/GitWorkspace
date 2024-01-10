from django.contrib import admin
from .models import Drink
from .models import Event

# Register your models here.
admin.site.register(Drink)
admin.site.register(Event)