from django.contrib import admin

from .models import *


admin.site.register(ApplicationStateModel)
admin.site.register(ApplicationForm)
admin.site.register(Reference)

