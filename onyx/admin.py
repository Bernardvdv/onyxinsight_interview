from django.contrib import admin

from .models import Data, Sensor


admin.site.register(Sensor)
admin.site.register(Data)
