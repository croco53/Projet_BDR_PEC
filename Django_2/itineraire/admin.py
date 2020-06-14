from django.contrib import admin

# Register your models here.
from .models import aero,comp,route

admin.site.register(aero)
admin.site.register(comp)
admin.site.register(route)
