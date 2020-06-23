from django.contrib import admin

# Register your models here.

from .models import *


admin.site.register(Aero)
admin.site.register(Comp)
admin.site.register(Route)
admin.site.register(Pays)